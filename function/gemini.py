import os 
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

gemini_api = os.environ.get('Bard_Api')
genai.configure(api_key=gemini_api)

def generate_response(question):
  response = model.generate_content(user, stream=True)
  for ans in response:
    return ans.text
