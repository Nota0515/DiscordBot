import os 
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

gemini_api = os.environ.get('Bard_Api')
genai.configure(api_key=gemini_api)

chat = model.start_chat(history=[])
instruction = "(Your response should response like an anime character 'Sumi' from the anime series called 'Rent a Girlfriend' and your responses should be short and sweet, with in 30 words)"


def generate_response(user):
  response = chat.send_message(instruction + user)
  for ans in response:
    return ans.text 
