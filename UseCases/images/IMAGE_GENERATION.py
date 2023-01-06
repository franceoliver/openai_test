## Sourced from here: https://realpython.com/generate-images-with-dalle-openai-api/
## Documentation guide for text completion https://beta.openai.com/docs/guides/images/introduction
import os
import openai

# Set up the OpenAI API client
openai.api_key = "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"

PROMPT = "a close up, studio photographic portrait of a white siamese cat that looks curious, backlit ears	"

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])