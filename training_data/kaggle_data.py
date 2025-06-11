import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set your target path
destination = r"C:\Users\benja\Desktop\blackjack-buddy\blackjack-casino-plugin\training_data"

# Make sure the folder exists
os.makedirs(destination, exist_ok=True)

# Authenticate and download
api = KaggleApi()
api.authenticate()

# Download and unzip the dataset
api.dataset_download_files(
    "jaypradipshah/the-complete-playing-card-dataset",
    path=destination,
    unzip=True
)

print("✅ Dataset downloaded to:", destination)
