<<<<<<< HEAD
import os
import shutil
import random

# Source folders (absolute paths)
src_images = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/Images/Images'
src_labels = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/YOLO_Annotations/YOLO_Annotations'

# Destination folders (absolute paths)
dst_images_train = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Images/train'
dst_images_val = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Images/val'
dst_labels_train = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Labels/train'
dst_labels_val = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Labels/val'

# Create destination folders if they don't exist
for d in [dst_images_train, dst_images_val, dst_labels_train, dst_labels_val]:
    os.makedirs(d, exist_ok=True)

# List all images (jpg and png)
all_images = [f for f in os.listdir(src_images) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(all_images)

# 80/20 train/val split
split_idx = int(0.8 * len(all_images))
train_images = all_images[:split_idx]
val_images = all_images[split_idx:]

def move_files(images, dst_img, dst_lbl):
    for img in images:
        base = os.path.splitext(img)[0]
        label = base + '.txt'
        src_img_path = os.path.join(src_images, img)
        src_lbl_path = os.path.join(src_labels, label)
        dst_img_path = os.path.join(dst_img, img)
        dst_lbl_path = os.path.join(dst_lbl, label)
        if os.path.exists(src_img_path) and os.path.exists(src_lbl_path):
            shutil.copy(src_img_path, dst_img_path)
            shutil.copy(src_lbl_path, dst_lbl_path)
        else:
            print(f"Warning: Missing image or label for {img}")

move_files(train_images, dst_images_train, dst_labels_train)
move_files(val_images, dst_images_val, dst_labels_val)

print("✅ Dataset organized for YOLOv5!")
=======
import os
import shutil
import random

# Source folders (absolute paths)
src_images = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/Images/Images'
src_labels = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/YOLO_Annotations/YOLO_Annotations'

# Destination folders (absolute paths)
dst_images_train = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Images/train'
dst_images_val = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Images/val'
dst_labels_train = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Labels/train'
dst_labels_val = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Labels/val'

# Create destination folders if they don't exist
for d in [dst_images_train, dst_images_val, dst_labels_train, dst_labels_val]:
    os.makedirs(d, exist_ok=True)

# List all images (jpg and png)
all_images = [f for f in os.listdir(src_images) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(all_images)

# 80/20 train/val split
split_idx = int(0.8 * len(all_images))
train_images = all_images[:split_idx]
val_images = all_images[split_idx:]

def move_files(images, dst_img, dst_lbl):
    for img in images:
        base = os.path.splitext(img)[0]
        label = base + '.txt'
        src_img_path = os.path.join(src_images, img)
        src_lbl_path = os.path.join(src_labels, label)
        dst_img_path = os.path.join(dst_img, img)
        dst_lbl_path = os.path.join(dst_lbl, label)
        if os.path.exists(src_img_path) and os.path.exists(src_lbl_path):
            shutil.copy(src_img_path, dst_img_path)
            shutil.copy(src_lbl_path, dst_lbl_path)
        else:
            print(f"Warning: Missing image or label for {img}")

move_files(train_images, dst_images_train, dst_labels_train)
move_files(val_images, dst_images_val, dst_labels_val)

print("✅ Dataset organized for YOLOv5!")
>>>>>>> 81189add828c30b4502f53de01b6c2e363570616
