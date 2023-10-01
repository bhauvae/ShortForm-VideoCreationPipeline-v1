import subprocess
import os
from variables.constants import ffmpeg


def concatenate_video_audio(video_object):
    video_file = video_object.video_file
    audio_file = video_object.audio_file
    output_file = video_object.temp
    time_offset = video_object.video_title_duration  # Offset in seconds

    # Delay the audio by the specified time_offset in milliseconds
    cmd = [
        ffmpeg,
        "-loglevel",
        "quiet",
        "-i",
        video_file,
        "-i",
        audio_file,
        "-c:v",
        "copy",
        "-af",
        f"adelay={int(time_offset * 1000)}|{int(time_offset * 1000)}",
        "-c:a",
        "aac",
        "-strict",
        "experimental",
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-shortest",
        "-y",
        output_file,
    ]

    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.replace(output_file, video_file)
