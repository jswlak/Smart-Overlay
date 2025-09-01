import cv2, os
from config import INPUT_VIDEO, OUTPUT_FOLDER

def open_video():
    cap = cv2.VideoCapture(INPUT_VIDEO)
    if not cap.isOpened():
        raise RuntimeError("❌ Error: Could not open input video.")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return cap, fps, width, height

def create_writer(fps, width, height):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    codecs = [
        ('mp4v', 'final_output.mp4'),
        ('XVID', 'final_output_xvid.avi'),
        ('MJPG', 'final_output_mjpg.avi')
    ]

    for codec, filename in codecs:
        fourcc = cv2.VideoWriter_fourcc(*codec)
        path = os.path.join(OUTPUT_FOLDER, filename)
        out = cv2.VideoWriter(path, fourcc, fps, (width, height))
        if out.isOpened():
            print(f"✅ Using codec {codec}, saving to {path}")
            return out, path
        else:
            print(f"⚠️ Codec {codec} failed, trying next...")

    raise RuntimeError("❌ Error: Could not open any VideoWriter.")
