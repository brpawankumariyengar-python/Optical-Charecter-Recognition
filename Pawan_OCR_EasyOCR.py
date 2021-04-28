import easyocr
import cv2 as Dekho
import pyttsx3

Bolna =""

Computer__Ankh = Dekho.VideoCapture(0)

check, Chitra = Computer__Ankh.read()

Ranheen_Chitra = Dekho.cvtColor(Chitra, Dekho.COLOR_BGR2GRAY)

Padna__Image = Chitra

Dekho.imshow("Tasveer",Chitra)

Dekho.waitKey(0)

Computer__Ankh.release()



Padaku = easyocr.Reader(['en'], gpu = False)
Padhai = Padaku.readtext(Padna__Image)

for x in Padhai:
	print(x[1])
	Bolna = Bolna + x[1]

voice_engine = pyttsx3.init()
voice_engine.say(Bolna)
voice_engine.runAndWait()
