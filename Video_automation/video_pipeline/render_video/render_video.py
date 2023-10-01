from .normalize_duration import normalize_duration
from .crop_background_clip import crop_background_clip
from .create_title import create_title
from .concatenate_video_audio import concatenate_video_audio
from .create_persistent_heading import create_persistent_heading
from .render_text import render_text


def render_video(video_object):
    normalize_duration(video_object)
    crop_background_clip(video_object)
    create_title(video_object)
    concatenate_video_audio(video_object) # not concatenating to the shortest length
    create_persistent_heading(video_object)
    render_text(video_object)
