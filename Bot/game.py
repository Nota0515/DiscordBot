import random
def winner(user,comp):
  if (user==comp):
    return "It's a tie :( "
  elif (user=="rock"):
    if (comp=="paper"):
      return f"Yeh! You win 🎊 :)\ncause I choose {comp}"
    else:
      return f"Bro sry...but I won \nbetter luck next time cause I choose {comp}😏"
  elif (user=="paper"):
    if (comp=="rock"):
      return f"😎 You win my dear🎊 \n cause I choose {comp} "
    else:
      return f"Sry but you loose cause I got {comp}"
  elif (user=="scissor"):
    if (comp=="paper"):
      return f"yeye!! you won bro 🎊\nCause I choose {comp}"
    else:
      return f"I won the match because of {comp}"

def game(user,comp):
  result = winner(user,comp)
  return result 
  
  