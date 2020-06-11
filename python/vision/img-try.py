from google.cloud import vision
client = vision.ImageAnnotatorClient()

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_secrets.json"

client = vision.ImageAnnotatorClient()

import io

path = 'Image.jpeg'
with io.open(path, 'rb') as image_file:
    content = image_file.read()
    image = vision.types.Image(content=content)

response = client.image_properties(image=image)
props = response.image_properties_annotation
print('Properties of the image:')

for color in props.dominant_colors.colors:
    print('Fraction: {}'.format(color.pixel_fraction))
    print('\tr: {}'.format(color.color.red))
    print('\tg: {}'.format(color.color.green))
    print('\tb: {}'.format(color.color.blue))