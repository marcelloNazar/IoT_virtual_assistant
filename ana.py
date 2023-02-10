import speech_recognition as sr
from playsound import playsound
import webbrowser as browser
from gtts import gTTS
from requests import get



palavraChave = 'ana'

def recebeAudio():
    while True:
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            print("Escutando: ")
            audio = microfone.listen(source)

        try:
            comando = (microfone.recognize_google(audio, language='pt-BR'))
            comando = comando.lower()
            if palavraChave in comando:
                print('Comando:' + comando)
                responde('bordao')
                executa(comando)
                break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return comando


def responde(resposta):
    playsound('./audios/'+str(resposta)+'.mp3')

def criaAudio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/mensagem.mp3')

    playsound('./audios/mensagem.mp3')


def executa(comando):
    if 'toca' in comando and 'chorão':
        spotify('chorão')
    elif 'previsão' in comando:
        tempo()
    elif 'tempo' in comando:
        tempo()
    else:
        responde('invalido')


def spotify(artista):
    if artista == 'chorão':
        browser.open('https://open.spotify.com/track/0qhwZ19NLe1FpQSmb4ZZau?si=377f3fddf40b4654')


def tempo():
    url = get('https://api.openweathermap.org/data/2.5/weather?q=pitangui&appid=5fe5da65b64464b5894adc9a62dedc15&units=metric&lang=pt_br')
    clima = url.json()
    
    temperatura = clima['main']['temp']
    previsão = clima['weather'][0]['description']
    ##print(temperatura, previsão)
    audio =  f'A temperatura é de {temperatura} graus com o tempo {previsão}'

    criaAudio(audio)


recebeAudio()
