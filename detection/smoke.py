from ultralytics import YOLO
from config import SMOKE_MODEL_PATH, CONF_THRESHOLD

smoke_model = YOLO(SMOKE_MODEL_PATH)

def detect_smoke(frame):
    results = smoke_model.predict(frame, conf=CONF_THRESHOLD, verbose=False)
    return any(len(r.boxes) > 0 for r in results)


