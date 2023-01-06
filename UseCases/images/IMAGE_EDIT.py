# https://beta.openai.com/docs/guides/images/usage
# Starting at Operating on edits

from io import BytesIO
from PIL import Image
import openai

# Set up the OpenAI API client
openai.api_key = "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"

## Read the image file from disk and resize it
# Read in source image to resize it to input size
image = Image.open("/Users/oliverfrance/Documents/repos/openai_test/DATA/input/sample_images/ollie_headshot.png")
width, height = 256, 256
image = image.resize((width, height))
## Save two version of the image
image.save("/Users/oliverfrance/Documents/repos/openai_test/DATA/input/image_edit_samples/edits_test.png")
# Open the _mask version and cut what you want out of it
image.save("/Users/oliverfrance/Documents/repos/openai_test/DATA/input/image_edit_samples/edits_test_mask.png")

response = openai.Image.create_edit(
  image=open("/Users/oliverfrance/Documents/repos/openai_test/DATA/input/image_edit_samples/edits_test.png", "rb"),
  mask=open("/Users/oliverfrance/Documents/repos/openai_test/DATA/input/image_edit_samples/edits_test_mask.png", "rb"),
  prompt="A moster attacking the towers" ,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(response['data'][0]['url'])
