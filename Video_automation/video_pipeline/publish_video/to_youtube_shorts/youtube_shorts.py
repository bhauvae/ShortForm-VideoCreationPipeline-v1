import os
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request

# Define the scopes and API version
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


def authenticate():
    creds = None

    # The file token.json stores the user's access and refresh tokens
    if os.path.exists(
        "Video_automation\\credentials\\youtube\\tokens.json"
    ):
        creds = Credentials.from_authorized_user_file(
            "Video_automation\\credentials\\youtube\\tokens.json",
            SCOPES,
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())

            except RefreshError:
                print("Error refreshing credentials.")
                return None
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "Video_automation\\credentials\\youtube\\credentials.json",
                SCOPES,
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(
            "Video_automation\\credentials\\youtube\\tokens.json",
            "w",
        ) as token:
            token.write(creds.to_json())

    return creds


def upload_shorts_video(
    credentials, video_path, video_title, video_description, video_tags
):
    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": video_title,
                "description": video_description,
                "tags": video_tags,
            },
            "status": {"privacyStatus": "public"},
        },
        media_body=media,
    )

    try:
        response = request.execute()
        print("Video uploaded:", response["id"])
        return response
    except googleapiclient.errors.HttpError as e:
        print("An error occurred:", e.content)


def publish_to_youtube_shorts(video_object):
    credentials = authenticate()
    shorts_tag = ["shorts"].extend(video_object.youtube_video_tags)
    if credentials:
        upload_shorts_video(
            credentials,
            video_object.video_file,
            video_object.name,
            video_object.youtube_video_description,
            shorts_tag,
        )
