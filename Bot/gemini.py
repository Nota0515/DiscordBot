import os 
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

gemini_api = os.environ.get('Bard_Api')
genai.configure(api_key=gemini_api)

def generate_response(user):
  response = model.generate_content(user)
  for ans in response:
    return ans.text 
