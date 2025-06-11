<<<<<<< HEAD
import torch
import numpy as np
from PIL import ImageGrab

class YoloScreenReader:
    def __init__(self, weights_path="yolov5/runs/train/exp/weights/best.pt"):
        self.model = torch.hub.load(
            "ultralytics/yolov5", "custom", path=weights_path, force_reload=True
        )

    def capture_screen(self, bbox=None):
        img = ImageGrab.grab(bbox=bbox)
        img_np = np.array(img)
        return img_np

    def detect_cards(self, bbox=None):
        frame = self.capture_screen(bbox)
        results = self.model(frame)
        cards = []
        for *box, conf, cls in results.xyxy[0]:
            x1, y1, x2, y2 = box
            label = self.model.names[int(cls)]
            cards.append({'label': label, 'x': float(x1)})
        return cards

    def recognize_cards_on_screen(self):
        """
        Detects cards on the screen and returns (player_cards, dealer_card).
        Sorts by x coordinate (left to right).
        """
        cards = self.detect_cards()
        if len(cards) >= 3:
            cards_sorted = sorted(cards, key=lambda c: c['x'])
            player_cards = [cards_sorted[0]['label'], cards_sorted[1]['label']]
            dealer_card = cards_sorted[2]['label']
            return player_cards, dealer_card
=======
import torch
import numpy as np
from PIL import ImageGrab

class YoloScreenReader:
    def __init__(self, weights_path="yolov5/runs/train/exp/weights/best.pt"):
        self.model = torch.hub.load(
            "ultralytics/yolov5", "custom", path=weights_path, force_reload=True
        )

    def capture_screen(self, bbox=None):
        img = ImageGrab.grab(bbox=bbox)
        img_np = np.array(img)
        return img_np

    def detect_cards(self, bbox=None):
        frame = self.capture_screen(bbox)
        results = self.model(frame)
        cards = []
        for *box, conf, cls in results.xyxy[0]:
            x1, y1, x2, y2 = box
            label = self.model.names[int(cls)]
            cards.append({'label': label, 'x': float(x1)})
        return cards

    def recognize_cards_on_screen(self):
        """
        Detects cards on the screen and returns (player_cards, dealer_card).
        Sorts by x coordinate (left to right).
        """
        cards = self.detect_cards()
        if len(cards) >= 3:
            cards_sorted = sorted(cards, key=lambda c: c['x'])
            player_cards = [cards_sorted[0]['label'], cards_sorted[1]['label']]
            dealer_card = cards_sorted[2]['label']
            return player_cards, dealer_card
>>>>>>> 81189add828c30b4502f53de01b6c2e363570616
        return None, None