from ultralytics import YOLO
from pathlib import Path


def main():
    # Use your dataset's data.yaml
    data_yaml = Path(r"D:\bone_fracture_yolo_app\bone_fracture_yolo_app\BoneFractureYolo\data.yaml")

    model = YOLO("yolov8n.pt")  # or yolov8s.pt etc.

    model.train(
        data=str(data_yaml),
        epochs=50,
        imgsz=640,
        batch=8,
        project="runs",
        name="train",
        verbose=True,
    )
    # best.pt will be at runs/detect/train/weights/best.pt


if __name__ == "__main__":
    main()
