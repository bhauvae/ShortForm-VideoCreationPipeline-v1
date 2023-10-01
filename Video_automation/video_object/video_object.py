from datetime import date


class Video:
    def __init__(self, name=None):
        self.name = name
        self.path = f"Video_automation\\video_pipeline\\temporary_files\\{self.name}"
        self.temp = f"{self.path}\\{self.name}_temp.mp4"
        self.video_file = f"{self.path}\\{self.name}.mp4"
        self.audio_file = f"{self.path}\\{self.name}.wav"
        self.text_file = f"{self.path}\\{self.name}.txt"
        self.subtitle_file = f"{self.path}\\{self.name}.ass"
        self.transcript_file = f"{self.path}\\{self.name}.json"

        self.video_duration = None
        self.video_width = None
        self.video_height = None
        self.video_title_duration = 2


class Quote_video(Video):
    def __init__(
        self,
        quote,
        pexels_video_query,
        youtube_video_tags,
        youtube_video_description,
        name=None,
        suffix="",
    ):
        if name is None:
            name = f"QUOTE-VIDEO_{str(date.today())}" + str(suffix)
            self.name = name
        else:
            self.name = name

        super().__init__(name)

        self.quote = quote
        self.pexels_video_query = pexels_video_query
        self.youtube_video_tags = youtube_video_tags
        self.youtube_video_description = youtube_video_description


class Reddit_readthrough_video(Video):
    pass


class Facts_video(Video):
    pass
