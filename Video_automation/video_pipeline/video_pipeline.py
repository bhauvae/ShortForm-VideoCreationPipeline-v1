import os

from video_pipeline.get_background_clip import download_background_clip
from video_pipeline.generate_audio import generate_audio
from video_pipeline.create_subtitle import create_subtitle
from video_pipeline.render_video import render_video
from video_pipeline.publish_video import publish_video


def create_quote_video(video_object):
    dir = video_object.path
    os.makedirs(dir, exist_ok=True)

    download_background_clip(video_object)
    generate_audio(video_object)
    create_subtitle(video_object)
    render_video(video_object)
    publish_video(video_object)

    return 0


def create_reddit_readthrough_video():
    pass


def create_facts_video():
    pass
