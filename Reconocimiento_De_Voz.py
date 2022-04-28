#Instruccion para descargar librerias externas --> py -m pip install modulo_a_instalar
#Descarga estos plugins si tienes problemas --> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio    pip install Flask 


#Importamos las librerias externas 
import speech_recognition as sr
import pyttsx3
import pywhatkit

#Nombre del "BOT"
Nombre = 'taquito'

#Variables extra
Escuchar = sr.Recognizer()
engine = pyttsx3.init()

#Selector de voces virtual
Voces = engine.getProperty('voices')
engine.setProperty('voice', Voces[1].id)

engine.say('Hola, ¿Que cancion te gustaria reproducir?')
engine.runAndWait()

def Hablar_BOT(text):
    engine.say(text)
    engine.runAndWait()

#Escuchamos al usuario e interpretamos el sonido 
def Escuchar_Usuario():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            Voz = Escuchar.listen(source)
            Grabar_Audio = Escuchar.recognize_google(Voz, language= 'es-MX')
            
            Grabar_Audio = Grabar_Audio.lower()
            if Nombre in Grabar_Audio:
                Grabar_Audio = Grabar_Audio.replace(Nombre, '')
                print(Grabar_Audio)

    except:
        pass
    return Grabar_Audio


def Buscador_Youtube():
    Grabar_Audio = Escuchar_Usuario()
    if 'reproduce' in Grabar_Audio:
        music = Grabar_Audio.replace('reproduce', '')
        Hablar_BOT('reproduciendo '+music)
        pywhatkit.playonyt(music)
        Hablar_BOT(Grabar_Audio)
Buscador_Youtube()

