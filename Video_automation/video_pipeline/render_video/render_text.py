import subprocess
import os
from variables.constants import ffmpeg


def render_text(video_object):
    input_video = video_object.video_file
    input_subtitle = (video_object.subtitle_file).encode("unicode_escape").decode()
    output_file = video_object.temp

    command = [
        ffmpeg,
        "-loglevel",
        "quiet",
        "-i",
        input_video,
        "-vf",
        f"ass='{input_subtitle}'",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-c:a",
        "copy",
        "-y",
        output_file,
    ]

    try:
        subprocess.run(command, check=True)

        os.replace(output_file, input_video)

        print("Subtitle rendering completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error during subtitle rendering:", e)
