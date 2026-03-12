# Tennis Analysis Project

A comprehensive computer vision project for analyzing tennis matches, including ball tracking, player detection, court line detection, and mini-court visualization.

## Features

- **Ball Tracking**: Real-time tennis ball detection and trajectory analysis
- **Player Detection**: YOLO-based player tracking and positioning
- **Court Line Detection**: Automatic tennis court boundary identification
- **Mini Court Visualization**: Transforms full court to mini court view
- **Player Statistics**: Speed, distance, and performance metrics
- **Video Analysis**: Process input videos and generate annotated outputs

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Adityabhatt1002/Tennis_Analysis.git
   cd Tennis_Analysis
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download models:**
   ```bash
   python download_models.py
   ```

## Models

The project uses the following pre-trained models hosted on Hugging Face:

- **Keypoints Model** (`keypoints_model.pth`): Court keypoint detection
- **YOLO Best** (`yolo5_best.pt`): Player and ball detection (best performing)
- **YOLO Last** (`yolo5_last.pt`): Player and ball detection (latest training)

Models are automatically downloaded when you run `download_models.py`.

**Direct Download Links:**
- [keypoints_model.pth](https://huggingface.co/AdityaB1002/Tennis-Analysis-Model/resolve/main/keypoints_model.pth)
- [yolo5_best.pt](https://huggingface.co/AdityaB1002/Tennis-Analysis-Model/resolve/main/yolo5_best.pt)
- [yolo5_last.pt](https://huggingface.co/AdityaB1002/Tennis-Analysis-Model/resolve/main/yolo5_last.pt)

## Usage

1. **Prepare input video:**
   Place your tennis match video in the `input_video/` folder.

2. **Run analysis:**
   ```bash
   python main.py
   ```

3. **View results:**
   Processed videos will be saved in the `output_videos/` folder.

## Project Structure

```
Tennis_Analysis/
├── main.py                    # Main execution script
├── yolo_inference.py          # YOLO model inference
├── download_models.py         # Model download script
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore rules
├── analysis/
│   └── ball_analysis.ipynb    # Ball trajectory analysis notebook
├── constants/
│   └── __init__.py
├── court_line_detector/
│   ├── court_line_detector.py
│   └── __init__.py
├── input_video/               # Place input videos here
├── mini_court/
│   ├── mini_court.py
│   └── __init__.py
├── models/                    # Models downloaded here (gitignored)
├── output_videos/             # Processed videos saved here
├── trackers/
│   ├── ball_tracker.py
│   ├── player_tracker.py
│   └── __init__.py
├── training/
│   ├── tennis_court_keypoints_training.ipynb
│   ├── tennis_training.ipynb
│   └── tennis-ball-detection-6/
├── utils/
│   ├── bbox_utils.py
│   ├── conversions.py
│   ├── player_stats_drawer_utils.py
│   ├── video_utils.py
│   └── __init__.py
└── yolov8x.pt                 # YOLOv8 model (gitignored)
```

## Demo Video

[Add your demo video link here - YouTube, Google Drive, etc.]

## Technologies Used

- **Python 3.8+**
- **OpenCV**: Computer vision and video processing
- **PyTorch**: Deep learning framework
- **YOLOv5/YOLOv8**: Object detection
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLO models trained on custom tennis datasets
- Court keypoint detection model for tennis court analysis
- Open-source computer vision community
