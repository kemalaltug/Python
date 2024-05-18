import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

kayit= sr.Recognizer()

def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon=kayit.listen(kaynak)
        ses= ""

        try:
            ses=kayit.recognize_google(mikrofon,language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım.")
        except sr.RequestError:
            print("Asistan: Sistem şu anda çalışmıyor.")
        return ses
    
def konusma(metin):
    tts=gTTS(text=metin,lang="tr",slow=False)
    ses="konusma.mp3"
    tts.save(ses)
    playsound(ses)
    os.remove(ses)


def yanit(ses):
    if "merhaba"in ses:
        konusma("Sanada merhaba canım")
    if "kapan"in ses:
        konusma("Çıkış Yapılıyor.")
        quit()
    if "nasılsın"in ses:
        konusma("iyiyim sen")
    
    if "çağlar nasıl biri"in ses:
        konusma("Çağları tanımıyorum")



konusma("canım neredesin")
print("Sistem Başlatıldı.")

while True:
    ses= dinleme()
    if bool(ses)==True:
        print(ses)
        ses=ses.lower()
        yanit(ses)



