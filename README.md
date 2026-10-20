# Bone Fracture Detection Using Deep Learning

A computer vision project that uses **YOLOv8** to detect and localize suspected bone fracture regions in X-ray images. The project integrates a trained object detection model with a **Flask web application** to display prediction results, bounding boxes, and confidence scores.

This project demonstrates the practical application of deep learning, image processing, and web development in medical image analysis.

## Project Overview

Bone fractures are commonly examined using X-ray images. Identifying fracture regions can be challenging and requires appropriate medical expertise.

This project explores an automated approach to detecting suspected fracture regions using the YOLOv8 object detection algorithm. The model processes X-ray images and predicts the locations of suspected fractures. A Flask-based web interface allows users to upload images and view the resulting predictions.

The system is developed as an academic prototype to demonstrate how deep learning can be applied to medical image analysis.

## Objectives

- Develop a deep learning-based bone fracture detection system.
- Apply YOLOv8 object detection to bone X-ray images.
- Identify and highlight suspected fracture regions using bounding boxes.
- Display predicted labels and confidence scores.
- Integrate the trained model into a Flask web application.
- Demonstrate a practical computer vision workflow.

## Key Features

- **X-ray Image Upload:** Upload bone X-ray images through a web interface.
- **Fracture Detection:** Analyze images using trained YOLOv8 model weights.
- **Bounding Box Visualization:** Highlight regions predicted by the model.
- **Confidence Scores:** Display the confidence associated with predictions.
- **Web Interface:** View detection results through a Flask application.
- **Modular Codebase:** Separate application code, model weights, dependencies, and dataset configuration.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development and model integration |
| YOLOv8 | Object detection |
| Ultralytics | YOLO model framework |
| Flask | Web application backend |
| OpenCV | Image processing |
| HTML and CSS | Web interface |
| Roboflow | Dataset preparation and management |
| Git and GitHub | Version control and source code hosting |

## System Workflow

1. **Input:** The user uploads a bone X-ray image.
2. **Image Processing:** The image is prepared for model inference.
3. **Model Inference:** YOLOv8 processes the image.
4. **Detection:** The model predicts suspected fracture regions.
5. **Visualization:** The application displays the output with bounding boxes and prediction information.

## Dataset

The bone X-ray dataset was obtained and managed using **Roboflow**, as described in the project report.

The dataset is organized into training, validation, and testing subsets for model development and evaluation. The images and annotations are prepared for YOLO-format object detection.

The dataset is not included in this repository by default. Anyone reproducing the project should obtain the appropriate dataset, review its license and usage conditions, and configure the dataset paths before training.

## Model Information

The project uses **YOLOv8** for object detection.

The repository includes `yolov8n.pt`, which provides the base YOLOv8 model weights. The web application expects the project's trained weights at:

`runs/detect/train/weights/best.pt`

The base weights and trained weights serve different purposes. The trained `best.pt` file is required for the application's intended fracture detection inference.

**Note:** The trained weights may need to be obtained separately if they are not included in the repository.

## Project Structure

```text
bone-fracture-yolo-app/
├── app.py
├── train_yolov8_detect.py
├── yolov8n.pt
├── requirements.txt
├── data/
├── templates/
├── static/
└── runs/
    └── detect/
        └── train/
            └── weights/
                └── best.pt
```

*Note: This represents the expected application layout. Some folders, including `runs/` and the trained weights, may be absent from a fresh GitHub clone.*

## Installation and Setup

### Prerequisites

- Python
- Git
- Required Python packages
- Trained YOLOv8 weights for inference

### 1. Clone the repository

```bash
git clone https://github.com/shivendrachaudhary9161/bone-fracture-yolo-app.git
cd bone-fracture-yolo-app
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the trained model

Ensure the trained `best.pt` file is available at:

```text
runs/detect/train/weights/best.pt
```

The application may fail during initialization if the file is missing because it loads the model when the Flask application starts.

### 6. Run the application

```bash
python app.py
```

Open the following address in your browser:

http://127.0.0.1:5000

Upload an X-ray image to view the detection output.

## Training the Model

The repository includes `train_yolov8_detect.py`, a model training script.

To retrain the model:

1. Obtain the dataset and check its usage license.
2. Configure the dataset YAML file with the correct training, validation, and testing paths.
3. Verify that the paths in the training script match your local dataset structure.
4. Install the required dependencies.
5. Run the training script.

Review the training script and dataset configuration before starting training. Dataset paths may require changes on a different computer.

## Results and Evaluation

For supported input images, the application can display predicted fracture regions, bounding boxes, and confidence scores.

Model performance should be assessed using suitable evaluation metrics, such as precision, recall, and mean Average Precision (mAP), based on validation or independent test data. Confidence scores alone do not establish diagnostic accuracy.

## Limitations

- Detection performance depends on the quality and diversity of the dataset.
- Blurred or low-quality X-ray images may affect predictions.
- Trained model weights are required to run inference.
- Training requires the dataset and a correctly configured YAML file.
- The system has not been clinically validated.

## Future Scope

- Evaluate the model on larger and more diverse X-ray datasets.
- Improve performance through systematic training and evaluation.
- Make dataset and model configuration easier to reproduce.
- Improve application error handling and deployment.
- Add documented evaluation results and automated tests.

## Disclaimer

This project is an academic prototype intended for educational purposes. It is not a clinically validated medical diagnostic system and must not replace assessment by a qualified medical professional.

## Author

**Shivendra Chaudhary**

GitHub: [shivendrachaudhary9161](https://github.com/shivendrachaudhary9161)

## Repository

[Bone Fracture Detection Using Deep Learning](https://github.com/shivendrachaudhary9161/bone-fracture-yolo-app)
