# -*- coding: utf-8 -*-
"""Number_Guessing_Game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19MUm0kOxVOHW0-2IQKiWZBUkJvgVOhKv
"""

import random
import sys
random=random.randint(1,100)
green = '\033[92m'
red = '\033[91m'
cross = '❌'
end = '\033[0m'
class NUM_GUESS:
  def __init__(self,Guess,Count,Num):
    self.Guess=Guess
    self.Count=Count
    self.Num=Num
  def game(self):
    for count in range(self.Count):
      self.Guess=int(input(f'"Guess Number" Attempt {count +1} is : '))
      if self.Guess == self.Num:
        print(f'Congratulation! you Guess the Number is :{self.Num}',end='')
        print(green + "✓" + end)
        break
      elif self.Guess < self.Num:
        print('TOO LOW')
      else:
        print('TOO HIGH')
    else:
      print()
      print(red + cross*5 + end)
      print(f'\U0001F923',end='')
      print(f'Sorry! you range out of attempts. the random number is : {self.Num}')
      print(f'Better Lucky Next Time ',end='')
      print("\U0001F44D")
find_num=NUM_GUESS(0,5,random)
find_num.game()

1