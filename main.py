import cv2
from config import *
from detection.smoke import detect_smoke
from utils.overlays import load_icon, apply_overlay
from utils.video_io import open_video, create_writer

# Load icon
icon = load_icon(OVERLAY_SMOKE_PATH, 15)
h_icon, w_icon = icon.shape[:2]

# Open video
cap, fps, width, height = open_video()
out, output_path = create_writer(fps, width, height)

# Overlay persistence
overlay_frames = OVERLAY_DURATION * fps
required_frames = int(PERSISTENCE_SEC * fps)
consecutive_hits = 0
overlay_counter = 0

print("▶️ Processing video...")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Smoke detection
    if detect_smoke(frame):
        consecutive_hits += 1
    else:
        consecutive_hits = 0

    if consecutive_hits >= required_frames:
        overlay_counter = overlay_frames
        consecutive_hits = 0

    # Apply overlay if active
    if overlay_counter > 0:
        overlay_counter -= 1
        frame = apply_overlay(frame, icon, 20, height - h_icon - 20)

    out.write(frame)

cap.release()
out.release()
print(f"🎉 Done! Saved processed video -> {output_path}")

