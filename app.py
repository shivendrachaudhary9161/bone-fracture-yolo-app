from pathlib import Path
import cv2
from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

MODEL_WEIGHTS = BASE_DIR / "runs" / "detect" / "train" / "weights" / "best.pt"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)

# Load model
model = YOLO(str(MODEL_WEIGHTS))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "xray_image" not in request.files:
        return redirect(url_for("index"))

    file = request.files["xray_image"]
    if file.filename == "":
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    save_path = UPLOAD_FOLDER / filename
    file.save(str(save_path))

    results = model(str(save_path), conf=0.1)

    r = results[0]
    img = cv2.imread(str(save_path))

    detections = []
    predicted = False

    if r.boxes is not None:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            label = r.names.get(cls_id, "fracture")

            # Draw box
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            text = f"{label} {conf:.2f}"
            cv2.putText(img, text, (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            detections.append({
                "label": label,
                "confidence": conf,
                "box": [int(x1), int(y1), int(x2), int(y2)]
            })

            predicted = True

    annotated_name = "annotated_" + filename
    annotated_path = UPLOAD_FOLDER / annotated_name
    cv2.imwrite(str(annotated_path), img)

    return render_template(
        "result.html",
        original_image=filename,
        annotated_image=annotated_name,
        predicted=predicted,
        detections=detections
    )


if __name__ == "__main__":
    app.run(debug=True)