# Blackjack Casino Plugin

## Overview
The Blackjack Casino Plugin is a Python desktop application that assists players in online Blackjack games by providing real-time advice based on cards detected on the screen. The plugin uses OpenCV and YOLOv5 to visually recognize playing cards and applies standard Blackjack strategy to offer actionable insights.

## Features
- Modern desktop GUI using [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- Screen capture and YOLOv5-based card recognition
- Real-time Blackjack strategy advice
- Easy integration with online gambling platforms

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/blackjack-casino-plugin.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd blackjack-casino-plugin
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## requirements.txt

```
opencv-python
numpy
Pillow
tk
customtkinter
torch
```

## Usage

1. **Install the tool in editable mode (optional, for development):**
   ```bash
   pip install -e .
   ```
2. **Run the application:**
   ```bash
   python src/blackjack_advisor.py
   ```
   or, if installed as a script:
   ```bash
   blackjack-advisor
   ```

## Packaging as a Desktop App (Windows)

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```
2. **Build the executable:**
   ```bash
   pyinstaller --onefile --windowed src\blackjack_advisor.py
   ```
3. **Find your app:**  
   The standalone `.exe` will be in the `dist` folder. You can move it to your Desktop or create a shortcut for easy access.

---

## Preparing Your Playing Card Dataset for YOLOv5

1. **Download the Dataset**
   - Use the provided `kaggle_data.py` script to download the playing card dataset from Kaggle:
     ```bash
     python training_data/kaggle_data.py
     ```

2. **Organize Images and Labels**
   - Use the `organize_cards_dataset.py` script to split your images into `train` and `val` sets:
     ```bash
     python organize_cards_dataset.py
     ```
   - Use the `copy_labels.py` script to copy the corresponding YOLO annotation `.txt` files to the correct folders:
     ```bash
     python copy_labels.py
     ```
   - Your folder structure should now look like:
     ```
     training_data/
       card_dataset/
         Images/
           train/
           val/
         Labels/
           train/
           val/
     ```

3. **Check Your Data Config**
   - Make sure your `cards.yaml` file points to the correct image folders:
     ```yaml
     train: ./training_data/card_dataset/Images/train
     val: ./training_data/card_dataset/Images/val
     nc: 52
     names: [ 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
              'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
              'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
              'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC' ]
     ```

4. **Train YOLOv5**
   - From the `yolov5` directory, run:
     ```bash
     python train.py --img 640 --batch 16 --epochs 50 --data ../cards.yaml --weights yolov5s.pt
     ```
   - After training, your best weights will be in `yolov5/runs/train/exp/weights/best.pt`.

5. **Update Your Application**
   - In your code, set the weights path to the trained model:
     ```python
     reader = YoloScreenReader(weights_path="yolov5/runs/train/exp/weights/best.pt")
     ```

---

**Tip:**  
If you add new images or annotations, rerun the organization and label copy scripts before retraining.

---

## Training Data

To enable robust card recognition, download or collect images of playing cards and place them in a folder named `training_data/Images` at the root of your project.

You can use datasets such as [The Complete Playing Card Dataset on Kaggle](https://www.kaggle.com/datasets/jaypradipshah/the-complete-playing-card-dataset/data) or your own screenshots.

**Example structure:**
```
blackjack-casino-plugin/
├── src/
├── training_data/
│   └── Images/
│       ├── 2_of_hearts.png
│       ├── 3_of_spades.png
│       └── ...
```
Organize images by card value or suit if you wish to use subfolders.

## Card Recognition

The app uses YOLOv5 to detect and classify cards based on the images in your dataset.  
Make sure your images are clear and labeled consistently.

## Next Steps

- Download and organize your card images in the `training_data/Images` folder.
- Use the provided scripts to split and organize your dataset for YOLOv5.
- Train your custom YOLOv5 model and update your application to use the new weights.
- The Blackjack advisor logic covers the full basic strategy for all hand types (hard, soft, and pairs).

## Modernization Ideas

- Modern UI with [customtkinter](https://github.com/TomSchimansky/CustomTkinter) or PyQt5
- Overlay advice directly on the game window
- Sound and notification support
- Customizable themes and hotkeys
- Voice feedback for hands-free play

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.