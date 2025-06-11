<<<<<<< HEAD
import os

def check_files(folder, allowed_exts):
    bad_files = []
    hidden_files = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.startswith('.'):
                hidden_files.append(os.path.join(root, f))
            ext = os.path.splitext(f)[1].lower()
            if ext not in allowed_exts:
                bad_files.append(os.path.join(root, f))
    return bad_files, hidden_files

# Set your paths here
images_dir = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Images/train'
labels_dir = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Labels/train'

# Check images
bad_imgs, hidden_imgs = check_files(images_dir, {'.jpg', '.jpeg', '.png'})
# Check labels
bad_lbls, hidden_lbls = check_files(labels_dir, {'.txt'})

print("Bad image files (not jpg/jpeg/png):", bad_imgs)
print("Hidden image files:", hidden_imgs)
print("Bad label files (not txt):", bad_lbls)
=======
import os

def check_files(folder, allowed_exts):
    bad_files = []
    hidden_files = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.startswith('.'):
                hidden_files.append(os.path.join(root, f))
            ext = os.path.splitext(f)[1].lower()
            if ext not in allowed_exts:
                bad_files.append(os.path.join(root, f))
    return bad_files, hidden_files

# Set your paths here
images_dir = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Images/train'
labels_dir = r'C:/Users/benja/Desktop/blackjack-buddy/blackjack-casino-plugin/training_data/card_dataset/Labels/train'

# Check images
bad_imgs, hidden_imgs = check_files(images_dir, {'.jpg', '.jpeg', '.png'})
# Check labels
bad_lbls, hidden_lbls = check_files(labels_dir, {'.txt'})

print("Bad image files (not jpg/jpeg/png):", bad_imgs)
print("Hidden image files:", hidden_imgs)
print("Bad label files (not txt):", bad_lbls)
>>>>>>> 81189add828c30b4502f53de01b6c2e363570616
print("Hidden label files:", hidden_lbls)