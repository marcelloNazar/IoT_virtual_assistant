from gtts import gTTS
from playsound import playsound


def criaAudio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/bordao.mp3')

    playsound('./audios/bordao.mp3')

criaAudio('ok, aguarde um segundo')