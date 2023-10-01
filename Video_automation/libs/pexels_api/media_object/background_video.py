import pandas as pd


class Background_clip:
    def __init__(self, json_video):
        self.__video = json_video

    @property
    def id(self):
        return int(self.__video["id"])

    @property
    def duration(self):
        return int(self.__video["duration"])

    @property
    def url(self):
        link = self.__video_files[self.__video_files["quality"] == "hd"].iloc[0]["link"]
        return link

    @property
    def __video_files(self):
        file_info = pd.DataFrame(self.__video["video_files"])
        file_info["res"] = file_info["width"] * file_info["height"]
        file_info = file_info.sort_values(by="res", ascending=False)
        file_info["type"] = file_info["file_type"].apply(lambda x: x.split("/")[0])
        file_info["format"] = file_info["file_type"].apply(lambda x: x.split("/")[-1])
        del file_info["file_type"]
        return file_info
