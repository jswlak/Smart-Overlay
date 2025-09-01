import cv2

def load_icon(path, scale_percent=15):
    icon = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if icon is None:
        raise FileNotFoundError(f"❌ Could not load overlay: {path}")
    w = int(icon.shape[1] * scale_percent / 100)
    h = int(icon.shape[0] * scale_percent / 100)
    return cv2.resize(icon, (w, h))

def apply_overlay(frame, icon, x_offset, y_offset):
    h, w = icon.shape[:2]

    # Prevent out-of-bounds errors
    if y_offset + h > frame.shape[0] or x_offset + w > frame.shape[1]:
        return frame  

    if icon.shape[2] == 4:  # has alpha channel
        alpha_s = icon[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        for c in range(3):
            frame[y_offset:y_offset+h, x_offset:x_offset+w, c] = (
                alpha_s * icon[:, :, c] +
                alpha_l * frame[y_offset:y_offset+h, x_offset:x_offset+w, c]
            )
    else:
        frame[y_offset:y_offset+h, x_offset:x_offset+w] = icon
    return frame
