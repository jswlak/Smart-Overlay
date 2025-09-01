from ultralytics import YOLO
from config import SMOKE_MODEL_PATH, CONF_THRESHOLD, LOG_INTERVAL

smoke_model = YOLO(SMOKE_MODEL_PATH)
frame_count = 0  # global counter for frames

def detect_smoke(frame):

    global frame_count
    frame_count += 1

    results = smoke_model.predict(frame, conf=CONF_THRESHOLD, verbose=False)

    # Optional: log speed info every N frames
    if frame_count % LOG_INTERVAL == 0:
        speed = results[0].speed  # dict with preprocess, inference, postprocess
        print(f"[Frame {frame_count}] Speed(ms): {speed}")

    # Return True if any detection exists  
    return any(len(r.boxes) > 0 for r in results)


