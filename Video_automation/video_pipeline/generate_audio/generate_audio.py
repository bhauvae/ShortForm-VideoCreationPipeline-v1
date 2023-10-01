from elevenlabs_unleashed.manager import ELUAccountManager
from elevenlabs import generate, save, set_api_key, play, api

import soundfile
from decouple import config


def generate_audio(video_object):
    eluac = ELUAccountManager(set_api_key, nb_accounts=2)  # Creates a queue of API keys
    eluac.next()  # First call will block the thread until keys are generated, and call set_api_key

    audio_file = video_object.audio_file

    text = video_object.quote

    """
    Will automatically generate 2 accounts in 2 threads. Takes a few seconds.
    """

    audio = generate(text=text, voice="Bella", model="eleven_multilingual_v1")

    save(
        audio=audio,
        filename=audio_file,
    )

    data, samplerate = soundfile.read(audio_file)
    soundfile.write(audio_file, data, samplerate)
