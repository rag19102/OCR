import io 
from PIL import Image
import pytesseract 
#from magickwand.image import Image as  wa

from wand.image import Image

from pdf2image import convert_from_path
pages = convert_from_path('3_RaghavendraRao.pdf', 500)

# f = "3_RaghavendraRao.pdf"
# with(Image(filename=f, resolution=120)) as source: 
#     for i, image in enumerate(source.sequence):
#         newfilename = f[:-4] + str(i + 1) + '.jpeg'
#         Image(image).save(filename=newfilename)

#file1 = open("G:\OCRPROJECT\OCR\\3_RaghavendraRao.pdf")
# pdfFile = wa("G:\OCRPROJECT\OCR\\3_RaghavendraRao.pdf", reso)
# pdfToImage = pdf.convert('jpeg')

# pagesOfPdf = []
# for image in pdfToImage:
#     imgPage = wa(image = image)
#     pagesOfPdf.append(imgPage.make_blob('jpeg'))


# text = []

# for imagePage in pagesOfPdf:
#     im = Image.open(io.BytesIO(imagePage))
#     recognizedText = pytesseract.image_to_string(im, lang = 'eng')
#     text,append(recognizedText)

# print(text)
