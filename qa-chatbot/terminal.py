import google.generativeai as genai 
from dotenv import load_dotenv
import os


load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# main chat loop
while True:

# Get user input from terminal
# user_input = input("Enter your message: ")
    user_input = input("\nEnter your question (or 'quit' to exit): ")


    # check if user wants to quit
    if user_input.lower() == 'quit':
        print("Thanks for chatting Goodbye!")
        break

# response = model.generate_content("Teach me about how an LLM works?")
# response = model.generate_content("Hello, my name is Waqar")


# Generate response using user's terminal/input
    response = model.generate_content(user_input)

# print(response.text)
    print("\nResponse:", response.text)