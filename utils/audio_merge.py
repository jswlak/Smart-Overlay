import os
import sys
from moviepy.editor import VideoFileClip, AudioFileClip

# Ensure project root is on sys.path for `config` import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_FOLDER, AUDIO_OUTPUT_PATH

def merge_audio_with_video(
    intermediate_video_name="final_output.mp4",
    final_video_name="final_output_video_with_audio_done.mp4"
):
    """
    Merge extracted audio with the processed video.

    Args:
        intermediate_video_name (str): filename of processed video (without audio)
        final_video_name (str): filename for final merged video
    Returns:
        str | None: path to the final video or None if failed
    """

    intermediate_video_path = os.path.join(OUTPUT_FOLDER, intermediate_video_name)
    final_video_path = os.path.join(OUTPUT_FOLDER, final_video_name)

    # Load the clips
    try:
        video_clip = VideoFileClip(intermediate_video_path)
        audio_clip = AudioFileClip(AUDIO_OUTPUT_PATH)
    except Exception as e:
        print(f"❌ Error loading video or audio clip: {e}")
        return None

    if video_clip is not None and audio_clip is not None:
        try:
            # Set the audio of the video clip
            final_clip = video_clip.set_audio(audio_clip)

            # Write the combined video file
            final_clip.write_videofile(final_video_path, codec="libx264", audio_codec="aac")
            print(f"✅ Successfully combined video and audio, saved to {final_video_path}")
            return final_video_path

        except Exception as e:
            print(f"❌ Error writing final video file: {e}")
            return None
        finally:
            # Close the clips
            video_clip.close()
            audio_clip.close()
            final_clip.close()
    else:
        if video_clip:
            video_clip.close()
        if audio_clip:
            audio_clip.close()
        return None
