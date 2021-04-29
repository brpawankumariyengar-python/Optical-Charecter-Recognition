# Converting PDF to images
from pdf2image import convert_from_path as PDF__Padh # We import pdf2image to convert pages in pdf file to jpg images that can be later on read with OCR

PDF_Wala_File = "/Users/brpawankumar/Desktop/Sample_PDF_File.pdf" # Here we store the path of the PDF File in the variable PDF_Wala_File

Panna = PDF__Padh(PDF_Wala_File) #Here we are converting the pages of PDF to Images

#Details of the Module can be accessed via link : https://pypi.org/project/pdf2image/

Page_Ka_Number = 1 # We declare a variable to store page numbers 

for Panna_Ankh in Panna:
	# Declaring filename for each page of PDF as JPG
	# For each page, filename will be:
	# PDF page 1 -> page_1.jpg
	# PDF page 2 -> page_2.jpg
	# PDF page 3 -> page_3.jpg
	# ....
	# PDF page n -> page_n.jpg

	Image_File_Ka_Naam = "Page_Number_"+str(Page_Ka_Number)+".jpg"

	Panna_Ankh.save(Image_File_Ka_Naam, 'JPEG') # Save the image of the page in system

	Page_Ka_Number  = Page_Ka_Number  + 1 # Increment the variable "Page_Ka_Number" so that we can create file namne for next page


print("Done")