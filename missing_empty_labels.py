import os

img_dir = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Images/train'
lbl_dir = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Labels/train'

missing = []
empty = []
for img in os.listdir(img_dir):
    if img.lower().endswith(('.jpg', '.jpeg', '.png')):
        base = os.path.splitext(img)[0]
        lbl = base + '.txt'
        lbl_path = os.path.join(lbl_dir, lbl)
        if not os.path.exists(lbl_path):
            missing.append(lbl)
        elif os.path.getsize(lbl_path) == 0:
            empty.append(lbl)

print("Missing label files:", missing)
print("Empty label files:", empty)