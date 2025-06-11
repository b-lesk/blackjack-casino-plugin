from PIL import ImageGrab
import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog

class ScreenReader:
    def __init__(self, templates_dir="training_data/Images"):
        self.templates = self.load_templates(templates_dir)

    def load_templates(self, templates_dir):
        templates = {}
        for fname in os.listdir(templates_dir):
            if fname.endswith(".png") or fname.endswith(".jpg"):
                label = os.path.splitext(fname)[0]
                img = cv2.imread(os.path.join(templates_dir, fname), 0)
                templates[label] = img
        return templates

    def capture_screen(self):
        # Capture the entire screen and convert to OpenCV format
        img = ImageGrab.grab()
        img_np = np.array(img)
        img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        return img_cv

    def recognize_card(self, card_img):
        card_img_gray = cv2.cvtColor(card_img, cv2.COLOR_BGR2GRAY)
        best_label = None
        best_val = 0
        for label, template in self.templates.items():
            res = cv2.matchTemplate(card_img_gray, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > best_val:
                best_val = max_val
                best_label = label
        return best_label if best_val > 0.7 else None  # 0.7 is a threshold, adjust as needed

    def analyze_screen(self):
        # Prompt user to select images for player's cards and dealer's card
        root = tk.Tk()
        root.withdraw()
        file_paths = filedialog.askopenfilenames(
            title="Select images for player's cards (select 2), then dealer's card (select 1)",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        if len(file_paths) < 3:
            print("Please select at least 3 images: 2 for player, 1 for dealer.")
            return []

        # Recognize cards
        recognized = []
        for path in file_paths:
            img = cv2.imread(path)
            label = self.recognize_card(img)
            recognized.append(label)
        # First two are player cards, last is dealer card
        return recognized[:2], recognized[2]

    def recognize_cards_on_screen(self):
        screen_img = self.capture_screen()
        found_cards = []
        for label, template in self.templates.items():
            res = cv2.matchTemplate(cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                found_cards.append(label)
                # Optionally, draw rectangles or mark found cards
        # Remove duplicates and return up to 3 cards (2 player, 1 dealer)
        found_cards = list(dict.fromkeys(found_cards))
        if len(found_cards) < 3:
            print("Could not detect at least 3 cards on the screen.")
            return [], None
        return found_cards[:2], found_cards[2]