import os
import requests
from pathlib import Path

# Define model URLs from Hugging Face
models = {
    "keypoints_model.pth": "https://huggingface.co/AdityaB1002/Tennis-Analysis-Model/resolve/main/keypoints_model.pth",
    "yolo5_best.pt": "https://huggingface.co/AdityaB1002/Tennis-Analysis-Model/resolve/main/yolo5_best.pt",
    "yolo5_last.pt": "https://huggingface.co/AdityaB1002/Tennis-Analysis-Model/resolve/main/yolo5_last.pt"
}

# Create models directory if it doesn't exist
models_dir = Path("models")
models_dir.mkdir(exist_ok=True)

# Download each model
for filename, url in models.items():
    filepath = models_dir / filename
    if not filepath.exists():
        print(f"Downloading {filename}...")
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Saved to {filepath}")
    else:
        print(f"{filename} already exists.")