import os  #for getting environment variables values
import chainlit as cl # for chatbot interface
import google.generativeai as genai # for google genai api
from dotenv import load_dotenv # for loading environment variables


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! how can I assist you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):

    prompt = message.content

    response = model.generate_content(prompt)

    response_text = response.text if hasattr(response, "text") else ""

    await cl.Message(content=response_text).send()