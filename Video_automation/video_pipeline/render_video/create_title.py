import subprocess
import os
from variables.constants import ffmpeg


def create_title(video_object):
    input_video = video_object.video_file
    output_file = video_object.temp
    title_text = video_object.name
    title_duration = video_object.video_title_duration

    command = [
        ffmpeg,
       "-loglevel",
        "quiet",
        "-i",
        input_video,
        "-vf",
        f"drawtext=fontfile= /Windows/fonts/calibri.ttf:text='{title_text}':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=24:fontcolor=white:box=1:boxcolor=black@0.5:boxborderw=5:enable='between(t,0,{title_duration})'",
        "-y",
        output_file,
    ]

    try:
        subprocess.run(command, check=True)
        os.replace(output_file, input_video)
        print("Finished")
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)
