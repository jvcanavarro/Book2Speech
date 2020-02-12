from gtts import gTTS


def get_audio(filename):
    text = open(filename, 'rb').read()
    output = filename[:-3] + '.wav'
    tts = gTTS(text, lang='pt')
    tts.save(output)
