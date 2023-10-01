import subprocess
import os
from variables.constants import ffmpeg, ffprobe


def get_duration(file_path):
    # Use ffprobe to get the duration of a media file in seconds
    cmd = [
        ffprobe,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        file_path,
    ]
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True
    )

    if result.returncode == 0:
        return float(result.stdout)
    else:
        raise Exception("Error while getting duration")


def normalize_duration(video_object):
    video_file = video_object.video_file
    output_file = video_object.temp

    audio_duration = get_duration(video_object.audio_file)
    title_duration = video_object.video_title_duration

    video_duration = audio_duration + title_duration + 0  # slight buffer

    cmd = [
        ffmpeg,
        "-loglevel",
        "quiet",
        "-stream_loop",
        "-1",  # Loop indefinitely
        "-i",
        video_file,
        "-t",
        str(video_duration),  # Set the desired duration
        "-c:v",
        "copy",
        "-y",
        output_file,
    ]

    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.replace(output_file, video_file)
    return 0
