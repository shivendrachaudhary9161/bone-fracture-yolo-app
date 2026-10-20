
from pathlib import Path
from ultralytics import YOLO


def main():
    # Locate the project directory
    project_dir = Path(__file__).resolve().parent

    # Dataset configuration
    data_yaml = project_dir / "data" / "bone_fracture.yaml"

    if not data_yaml.exists():
        raise FileNotFoundError(
            f"Dataset configuration not found: {data_yaml}"
        )

    # Load the YOLOv8 base model
    model = YOLO(str(project_dir / "yolov8n.pt"))

    # Train the model
    model.train(
        data=str(data_yaml),
        epochs=50,
        imgsz=640,
        batch=8,
        project=str(project_dir / "runs"),
        name="train",
        verbose=True,
    )


if __name__ == "__main__":
    main()
