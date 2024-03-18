import openai
import os 

openai.api_key = os.environ['Open_AI']

  
instruction = "Your response should response like an anime character 'Sumi' from the anime series called 'Rent a Girlfriend'"

def gpt(user):
  response = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'system', 'content': instruction},
              {"role": "user", "content": user}],
    #stream = True
    temperature = 0.2
  )
  return response.choices[0].message.content




  
if __name__=='__main__':
  quest = input("Enter prompt: ")
  responses = gpt(quest)
  print(responses)