from vosk import Model, KaldiRecognizer, SetLogLevel

from libs.rpunct import RestorePuncts

SetLogLevel(-1)

import wave, json


# TODO improve efficiency, dont read the complete file
def generate_transcript_file(video_object):
    audio_filename = video_object.audio_file
    print("transcribing")

    wf = wave.open(str(audio_filename), "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        exit(1)

    model = Model("Video_automation\\libs\\vosk-model-en-us-0.22")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    data = wf.readframes(wf.getnframes())

    rec.AcceptWaveform(data)
    data = json.loads(rec.Result())

    transcript_filename = video_object.transcript_file
    text_filename = video_object.text_file
    with open(transcript_filename, "w") as f:
        json.dump(data["result"], f)

    text = data["text"]

    punctuated = RestorePuncts().punctuate(text, lang="en")

    with open(text_filename, "w") as f:
        f.write(punctuated)
