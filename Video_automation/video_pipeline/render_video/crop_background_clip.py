import subprocess
import os
from variables.constants import ffmpeg, ffprobe


def crop_background_clip(video_object):
    max_height = 1920
    max_width = 1080
    input = video_object.video_file
    output = video_object.temp
    target_aspect_ratio = 9 / 16
    # Get input video resolution
    ffprobe_command = [
        ffprobe,
        "-v",
        "error",
        "-show_entries",
        "stream=width,height",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        input,
    ]

    try:
        result = subprocess.run(ffprobe_command, text=True, capture_output=True)
        width, height = map(int, result.stdout.strip().split("\n"))

        # Calculate crop dimensions to achieve 9:16 aspect ratio

        crop_height = min(height, int(width / target_aspect_ratio), max_height)
        crop_width = min(int(crop_height * target_aspect_ratio), max_width)

        command = [
            ffmpeg,
            "-loglevel",
            "quiet",
            "-i",
            input,
            "-vf",
            f"crop={str(crop_width)}:{str(crop_height)}",
            "-c:a",
            "copy",
            "-y",
            output,
        ]

        subprocess.run(command, check=True)
        os.replace(output, input)
        video_object.video_width = crop_width
        video_object.video_height = crop_height
        print("Finished")
    except subprocess.CalledProcessError as e:
        print("Error during cropping:", e)
    except Exception as e:
        print("Error:", e)
