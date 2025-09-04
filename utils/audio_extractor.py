import os
from moviepy.editor import VideoFileClip
from config import INPUT_VIDEO, OUTPUT_FOLDER, AUDIO_OUTPUT_PATH

def extract_audio():
    """Extract audio from input video and save as WAV."""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    try:
        video_clip = VideoFileClip(INPUT_VIDEO)
    except Exception as e:
        print(f"❌ Error loading video file: {e}")
        return None

    if video_clip.audio is not None:
        try:
            video_clip.audio.write_audiofile(AUDIO_OUTPUT_PATH, codec="pcm_s16le")
            print(f"✅ Successfully extracted audio to {AUDIO_OUTPUT_PATH}")
        except Exception as e:
            print(f"❌ Error writing audio file: {e}")
        finally:
            video_clip.audio.close()
            video_clip.close()
    else:
        print("⚠️ No audio track found in the video.")
        video_clip.close()

    return AUDIO_OUTPUT_PATH
