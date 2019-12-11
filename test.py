from google.cloud import vision
import io
import os
from google.oauth2 import service_account
#client = vision.ImageAnnotatorClient("Api_json.json")
#vision_client = vision.ImageAnnotatorClient('C:\\Users\\Sowjanya\\Downloads\\Api_json.json')
credentials = service_account.Credentials.from_service_account_file('C:\\Users\\Sowjanya\\Downloads\\Api_json.json')
print(credentials)

client = vision.ImageAnnotatorClient(credentials=credentials)
path = 'image.jpg'

with io.open(path, 'rb') as image_file:
        content = image_file.read()

image = vision.types.Image(content=content)
# response = client.image_properties(image=image)
# props = response.image_properties_annotation
# print('Properties of the image:')

# for color in props.dominant_colors.colors:
#     print('Fraction: {}'.format(color.pixel_fraction))
#     print('\tr: {}'.format(color.color.red))
#     print('\tg: {}'.format(color.color.green))
#     print('\tb: {}'.format(color.color.blue))

# import io 
# import os+6
# # Imports the Google Cloud client library
# from google.cloud import vision
# from google.cloud.vision import types
# # Instantiates a client
# client = vision.ImageAnnotatorClient()
# # The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'image.jpg')

# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
# image = types.Image(content=content)


# # Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations
# print('Labels:')
# for label in labels:
#     print(label.description)


#Code for text detection on images

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))