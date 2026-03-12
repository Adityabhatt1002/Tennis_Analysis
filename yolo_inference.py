from ultralytics import YOLO
model=YOLO('yolov8x')  # Load a pretrained YOLOv8n model
results=model.predict('input_video/image.png',save=True)  # Predict on an image and save the results