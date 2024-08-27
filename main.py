from openai import OpenAI

client = OpenAI(api_key='yourapikey')

def get_response(message):
  response = client.chat.completions.create(model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        message,
    ]

  )
  return response

question = input("Please say something")
message = {"role": "user", "content": question }

answer = get_response(message)

print(answer.choices[0].message.content)
