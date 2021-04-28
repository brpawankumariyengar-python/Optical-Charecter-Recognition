import cv2
import pytesseract
import pyttsx3

Bolna =""

#Computer__Ankh = cv2.VideoCapture(0)
#check, img = Computer__Ankh.read()

img = cv2.imread("image.png")

#Computer__Ankh.release()


def OCR_Core(img):
	text = pytesseract.image_to_string(img)
	return text

def GET_GRAYSCALE(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#def Remove_Noise(image):
	#return cv2.medianBlur(image, 5)

#def Thresholding(image):
	#return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = GET_GRAYSCALE(img)
#cv2.imshow("Tasveer grayscale", img)
##img = Remove_Noise(img)
#cv2.imshow("Tasveer remove noise" , img)
#cv2.waitKey(0)
#img = Thresholding(img)
#cv2.imshow("Tasveer threshold", img)
#cv2.waitKey(0)

Bolna = OCR_Core(img)

print(Bolna)

voice_engine = pyttsx3.init()
voice_engine.say(Bolna)
voice_engine.runAndWait()