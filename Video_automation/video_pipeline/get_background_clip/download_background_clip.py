import time
import requests
from libs.pexels_api import PEXELS_VIDEO_API
import pandas as pd
from decouple import config

MAX_VIDEOS_PER_QUERY = 100
RESULTS_PER_PAGE = 100
PAGE_LIMIT = MAX_VIDEOS_PER_QUERY / RESULTS_PER_PAGE
API_KEY = config("PEXELS_API_KEY")


def get_sleep(t):
    def sleep():
        time.sleep(t)

    return sleep


# TODO REFACTOR THIS SHIT, GET A LIST OF ALL VIDEO IDS
def find_background_clip(query):
    sleep = 0.1

    sleep = get_sleep(sleep)

    api = PEXELS_VIDEO_API(API_KEY)
    query = query

    page = 1

    archive = pd.DataFrame(columns=["id", "url", "duration", "query", "used"])

    # Step 1: Getting urls and meta information

    while page <= PAGE_LIMIT:
        api.search(query, page=page, results_per_page=RESULTS_PER_PAGE)
        videos = api.get_entries()

        for i, video in enumerate(videos):
            archive.loc[i] = [
                video.id,
                video.url,
                video.duration,
                query,
                False,
            ]

        if not api.has_next_page:
            break

        page += 1
        sleep()

    archive_path = "Video_automation\\archive\\clips.csv"
    with open(archive_path, "a") as f:
        archive.to_csv(f, index=False, header=False)

    # Clean-up
    data = pd.read_csv(archive_path)
    data.drop_duplicates(inplace=True)

    data.to_csv(archive_path, index=False, header=False, mode="w")


def retrieve_background_clip(video_object):
    archive_path = "Video_automation\\archive\\clips.csv"
    data = pd.read_csv(archive_path)
    data.columns = ["id", "url", "duration", "query", "used"]
    files = data[
        (data["used"] == False) & (data["query"] == video_object.pexels_video_query)
    ]
    files.reindex()

    # Step 2: Downloading
    id = files.iloc[0]["id"]
    url = files.iloc[0]["url"]

    video_path = video_object.video_file

    response = requests.get(url, stream=True)

    with open(video_path, "wb") as outfile:
        outfile.write(response.content)

    data.set_index("id", inplace=True)
    data.loc[id, "used"] = True
    data.reset_index(inplace=True)

    data.to_csv(archive_path, index=False, header=False, mode="w")


def download_background_clip(video_object):
    find_background_clip(video_object.pexels_video_query)
    retrieve_background_clip(video_object)
