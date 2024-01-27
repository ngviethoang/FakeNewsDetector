from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"), )


def get_chat_response(messages):
  chat_completion = client.chat.completions.create(
      messages=messages,
      model="gpt-4",
  )
  return chat_completion.choices[0].message.content
