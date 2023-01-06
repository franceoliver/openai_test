# https://beta.openai.com/docs/guides/images/language-specific-tips
# Starting at Operating on Image data

from io import BytesIO
from PIL import Image
import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Read the image file from disk and resize it
image = Image.open("/Users/oliverfrance/Documents/repos/openai_test/DATA/input/PHOTO-2022-11-02-20-29-53.jpg")
width, height = 256, 256
image = image.resize((width, height))
image.save("test.png")


# Convert the image to a BytesIO object
byte_stream = BytesIO()
image.save(byte_stream, format='PNG')
byte_array = byte_stream.getvalue()

response = openai.Image.create_variation(
  image=byte_array,
  n=1,
  size="1024x1024"
)
print(response['data'][0]['url'])
