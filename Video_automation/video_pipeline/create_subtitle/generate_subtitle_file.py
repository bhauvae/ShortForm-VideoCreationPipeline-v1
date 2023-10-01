import re
import pandas as pd
from datetime import datetime


def generate_subtitle_file(video_object):
    subtitle_filename = video_object.subtitle_file
    transcript_filename = video_object.transcript_file
    text_filename = video_object.text_file
    video_title = video_object.name
    title_duration = video_object.video_title_duration
    with open(text_filename, "r") as f:
        text = f.read()

    # RETAIN PUNCTUATIONS
    phrases = re.split(r"(?<=[,.!?])\s*", text)
    # Remove empty phrases
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]

    normalize = lambda text: re.sub(r"[\s\W_]+", "", text).lower()
    convtime = lambda seconds: datetime.utcfromtimestamp(seconds).strftime(
        "%H:%M:%S.%f"
    )[1:11]

    transcript = pd.read_json(transcript_filename)
    subtitle_data = pd.DataFrame(columns=["start", "end", "phrase"])
    for i, phrase in enumerate(phrases):
        sub_phrase = []
        sub_phrase_start_time = []
        sub_phrase_end_time = []
        for index, row in transcript.iterrows():
            sub_phrase.append(row["word"])
            sub_phrase_start_time.append(row["start"])
            sub_phrase_end_time.append(row["end"])
            transcript.drop(index, axis=0, inplace=True)

            sub_line = " ".join(sub_phrase)

            if normalize(phrase) == normalize(sub_line):
                subtitle_data.loc[i] = [
                    convtime(sub_phrase_start_time[0] + title_duration),
                    convtime(sub_phrase_end_time[-1] + title_duration),
                    phrase,
                ]
                break

    for i in range(1, len(subtitle_data)):
        subtitle_data.at[i, "start"] = subtitle_data.at[i - 1, "end"]
    print(subtitle_data)
    with open(subtitle_filename, "w", encoding="utf-8-sig") as subtitle_file:
        subtitle_file.write("[Script Info]\n")
        subtitle_file.write(f"Title: {video_title}\n")
        subtitle_file.write("ScriptType: v4.00+\n")
        subtitle_file.write("WrapStyle: 1\n")
        subtitle_file.write("[V4+ Styles]\n")
        subtitle_file.write(
            "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
        )
        subtitle_file.write(
            "Style: Default,Arial,24,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,1,5,10,10,10,1\n\n"
        )
        subtitle_file.write("[Events]\n")
        subtitle_file.write(
            "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
        )

        for index, subtitle in subtitle_data.iterrows():
            subtitle_file.write(
                f"Dialogue: 0,{subtitle['start']},{subtitle['end']},Default,,0,0,0,,{subtitle['phrase']}\n"
            )

        return 0
