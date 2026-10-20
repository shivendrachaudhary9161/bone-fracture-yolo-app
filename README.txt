
Bone Fracture Detection using YOLOv8 (Object Detection)
======================================================

Steps to use this code:

1. Create and activate a virtual environment (recommended), then install dependencies:

   pip install -r requirements.txt

2. Prepare your detection dataset in YOLO format. Example folder structure:

   BoneFractureYOLO/
     images/train/  # training images
     images/val/    # validation images
     labels/train/  # one .txt per image
     labels/val/

   Each labels/*.txt file contains lines in YOLO format:

     <class_id> <x_center> <y_center> <width> <height>

   All coordinates are normalized between 0 and 1. Use class_id 0 for "fracture".

3. Edit data/bone_fracture.yaml and set the correct path for `path:` if your
   dataset folder is not `../BoneFractureYOLO` relative to this project.

4. Train the YOLOv8 detection model:

   python train_yolov8_detect.py

   After training, the best weights will be saved to:

   runs/detect/train/weights/best.pt

5. Make sure app.py points to that weights file (MODEL_WEIGHTS constant).

6. Run the Flask app:

   python app.py

7. Open a browser at http://127.0.0.1:5000/ and upload an X-ray image.
   If a fracture is detected, the app will draw a GREEN bounding box around
   the fracture region and display the annotated image.
