from gtts import gTTS
from io import BytesIO


def text_to_speech(text, output, play_audio=False):
    tts = gTTS(' '.join(text), lang='pt', tld='com.br')
    tts.save(output + '.mp3')
    if play_audio:
        print('Playing audio...')
        mp3 = BytesIO()
        tts.write_to_fp(mp3)