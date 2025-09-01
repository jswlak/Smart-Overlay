# Configuration
INPUT_VIDEO = "input_videos/input.mp4"
OUTPUT_FOLDER = "output_videos"

SMOKE_MODEL_PATH = "models/smoke_detect.pt"
# ANIMAL_MODEL_PATH = "models/yolov8x-oiv7.pt"

OVERLAY_SMOKE_PATH = "overlays/no_smoking.png"
# OVERLAY_ANIMAL_PATH = "overlays/no_animal_harm.png"

CONF_THRESHOLD = 0.5
OVERLAY_DURATION = 3        # seconds
PERSISTENCE_SEC = 0.3       # seconds

# VALID_ANIMAL_CLASSES = {
#     "dog", "cat", "horse", "cow", "sheep", 
#     "elephant", "zebra", "giraffe", "bear", 
#     "dolphin", "mammal"
# }
