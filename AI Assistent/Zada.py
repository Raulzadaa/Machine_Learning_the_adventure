import pyttsx3
from datetime import datetime
import speech_recognition as sr
import os

engine = pyttsx3.init()

def speech(voz):

    rate = engine.getProperty('rate') # speed rate to speech
    engine.setProperty('rate' , 185)

    voices = engine.getProperty('voices') # select voice
    engine.setProperty('voice', voices[0].id)
    
    engine.say(voz)
    engine.runAndWait()

def hour():

    tempo = datetime.today().strftime("%I:%M")

    speech("agora são: ")
    speech(tempo)

def date():

    dia , mes , ano = datetime.today().strftime("%d %m %y").split(' ')

    speech("hoje é: ")
    speech(dia)
    speech("do" + str(int(mes)))
    speech("de" +ano)

def welcome():

    speech("Boas vindas meu soberano, sou o Zada")
    hour()
    date()

    x_hour = datetime.today().hour

    if x_hour >= 6 and x_hour < 12:
        speech("bom dia Raul")
    elif x_hour < 18:
        speech("boa tarde Raul")
    elif x_hour < 24:
        speech("boa noite Raul")
    else:
        speech("ta fazendo o que acordado uma hora dessas? ")
    speech("como posso lhe ajudar")

def microfone():

    reco = sr.Recognizer()

    with sr.Microphone() as source:
        reco.pause_threshold = 1
        audio = reco.listen(source)

    try:
        print("Reconhecendo a fala...")
        comand = reco.recognize_google(audio,language='pt-br')
        print(comand)
    
    except Exception as exce:
        print(exce)

        return "None"
    
    return comand

if __name__ == "__main__":
    while(True):
        print("escutando...")
        
        comand = microfone().lower()

        if 'roblox' in comand and 'abrir' in comand:
            print("abrindo o roblox")
            os.startfile(r'C:\Users\Adm\Desktop\Roblox Player')

        elif 'vavá'in comand and 'abrir' in comand:
            print("abrindo o valorant")
            os.startfile(r'C:\Users\Adm\Desktop\VALORANT')

        if 'desligar' in comand:
            exit()
