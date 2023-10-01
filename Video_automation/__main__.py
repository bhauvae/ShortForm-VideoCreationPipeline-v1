from video_object import Quote_video
from video_pipeline import create_quote_video
from datetime import date

if __name__ == "__main__":
    create_quote_video(
        Quote_video(
            quote="Stars are like the memories of the universe, each one a glimpse into its past. The mind is a canvas, and thoughts are the "
            "brushstrokes that paint our reality. In the symphony of life, each experience plays a note that resonates through eternity. Time "
            "is a river, and we are the stones that shape its flow. The dance of chaos and order births the cosmos. A smile is the "
            "gravitational pull of happiness on the fabric of existence. Echoes remind us that even sound leaves a piece of itself behind.",
            pexels_video_query="Law",
            youtube_video_tags=[],
            youtube_video_description="test",
        )
    )
# TODO USE THE VIMEO LINK DIRECTLY IN FFMPEG SUBPROCESS
# TODO VOSK IS WAYY TOO FUCKING SLOW
