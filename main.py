import openai

openai.api_key = 'your-api-key-here'

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how can I create a bot?"},
    ]
)

print(response.choices[0].message["content"])