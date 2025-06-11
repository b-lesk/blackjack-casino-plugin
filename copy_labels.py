import os
import shutil

# Set your paths
src_labels = r'training_data/YOLO_Annotations/YOLO_Annotations'
dst_labels_train = r'training_data/card_dataset/Labels/train'
dst_labels_val = r'training_data/card_dataset/Labels/val'
images_train = r'training_data/card_dataset/Images/train'
images_val = r'training_data/card_dataset/Images/val'

# Make sure destination folders exist
os.makedirs(dst_labels_train, exist_ok=True)
os.makedirs(dst_labels_val, exist_ok=True)

def copy_labels(images_folder, labels_folder, dst_folder):
    for img in os.listdir(images_folder):
        if img.lower().endswith(('.jpg', '.jpeg', '.png')):
            base = os.path.splitext(img)[0]
            label_file = base + '.txt'
            src_label_path = os.path.join(labels_folder, label_file)
            dst_label_path = os.path.join(dst_folder, label_file)
            if os.path.exists(src_label_path):
                shutil.copy(src_label_path, dst_label_path)
            else:
                print(f"Warning: Label file not found for {img}")

copy_labels(images_train, src_labels, dst_labels_train)
copy_labels(images_val, src_labels, dst_labels_val)

print("✅ All label files copied to train/val folders.")