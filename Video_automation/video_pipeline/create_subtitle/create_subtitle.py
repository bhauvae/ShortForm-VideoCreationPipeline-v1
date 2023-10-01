from .generate_transcript_file import generate_transcript_file
from .generate_subtitle_file import generate_subtitle_file

def create_subtitle(video_object):
    generate_transcript_file(video_object)
    generate_subtitle_file(video_object)
