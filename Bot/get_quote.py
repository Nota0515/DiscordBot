import requests
from bs4 import BeautifulSoup

def get_quote():
  req = requests.get("https://zenquotes.io")
  filter = BeautifulSoup(req.content, "html.parser")
  quote = filter.find("div",{"id":"carousel-quote-1"}).find('h1').text
  author = filter.find("div",{"id":"carousel-quote-1"}).find('p').string 
  return f"{quote} --by {author} "

if __name__== "__main__" :
  user = input("You want a quote y/n ")

  if user == 'y' or 'yes':
    quote = get_quote()
    print(quote)

  else:
    print("it seems like you don't want a quote,or may be its my fault :) ")
  
