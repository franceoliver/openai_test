## Sourced from here: https://www.codingthesmartway.com/how-to-use-chatgpt-with-python/
## Documentation guide for text completion https://beta.openai.com/docs/guides/completion
import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
# Models https://beta.openai.com/docs/models/overview
model_engine = "text-davinci-003"
prompt = "Today is friday"

# Generate a response https://beta.openai.com/docs/api-reference/models
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=4000,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(f"Ollie:'{prompt}'\n")
print(f"chatgpt:'{response.lstrip()}'")