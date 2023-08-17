#----------------------------#
#                            #
# math (auto)                 #
#                            #
# by nikhilhex               #
# finished october 17, 2022  #
#----------------------------#

import random
from colorama import Fore
from tabulate import tabulate
from art import text2art
from tqdm import trange
import sys
def convertable(string):
    try:
        float(string)

        return True
    except ValueError:
        return False

def crt(string):
  try:
    float(str(string).replace("/", ""))

    return True
  except ValueError:
    return False
def ehm():
  operation = random.choice(["x", "+", "-", "÷"])
  num1 = random.randint(1,(sys.maxsize / 2))
  num2 = random.randint(1,(sys.maxsize / 2))
  ans = input(f"{Fore.MAGENTA} What's {str(num1)} {operation} {str(num2)} \n")
  if operation == "x":
    crt = bool(ans == str(num1 * num2))
  elif operation == "+":
    crt = bool(ans == str(num1 + num2))
  elif operation == "-":
    crt = bool(ans == str(num1 - num2))
  elif operation == "÷":
    crt = bool(ans == str(num1 / num2))
    return crt
print(text2art("auto", font='3d_diagonal'))
print(text2art("by nikhilhex", font='bell'))
if True:

  mode = input(Fore.CYAN +
               "Select a mode (a/s/m/d/da/dm/ds/dd) \n")
  if mode == "a":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")
    if questions == 0:
      exit()
    correct = 0
    incorrect = 0
    for x in trange(int(questions)):

      num1 = random.randint(1, (x + 1))
      num2 = random.randint(1, (x + 1))
      print(
        f"{Fore.MAGENTA}Whats {str(num1)} + {str(num2)}? {Fore.CYAN}\n")
      ans = num1 + num2
      print(ans)
      if ans == "exit":
        exit()
      if ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == num1 + num2:
        print(f"{Fore.GREEN}Correct")
        correct = correct + 1
      else:
        print(Fore.RED + "INCORRECT" + Fore.CYAN + "The correct answer was: " + str(num1+num2))
        incorrect = incorrect + 1
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print("Great work! Restart this app to do another mode!")

  elif mode == "s":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    negative = input("Subtract negative numbers from negative numbers? (y/n) \n")
    if negative == "y":
      positive = input("Positive numbers also? (y/n) \n")

    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")

    if questions == 0:
      exit()

    correct = 0
    incorrect = 0
    
    for x in trange(int(questions)):
      num1 = 0
      num2 = 0
      if negative == "y" and positive == "y":
        num1 = random.randint(x * -1, x + 1)
        num2 = random.randint(x * -1, x + 1)
      elif negative == "y" and positive == "n":
        num1 = random.randint(x * -1, x * -1)
        num2 = random.randint(-x * -1, x * -1)
      elif negative == "n":
        num1 = random.randint(x, random.randint(x + 1, x + 20))
        num2 = random.randint(x, random.randint(x + 1, x + 20))
      print(f"{Fore.MAGENTA}What's {num1} - {num2}? \n")
      ans = num1 - num2
      print(ans)
      if ans == "exit":
        exit()
      elif ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == num1 - num2:
        correct = correct + 1
        print(Fore.GREEN + "Correct")
      else:
        incorrect = incorrect + 1
        print(Fore.RED + "INCORRECT" + Fore.CYAN + "The correct answer was: " + str(num1-num2))
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print(Fore.RED + "Great work! Restart this app to do another mode!")
  elif mode == "m":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")
    if questions == 0:
      exit()
    correct = 0
    incorrect = 0
    for x in trange(int(questions)):

      num1 = random.randint(1, (x + 1))
      num2 = random.randint(1, (x + 1))
      print(
        f"{Fore.MAGENTA}Whats {str(num1)} x {str(num2)}? {Fore.CYAN}\n")
      ans = num1 * num2
      print(ans)
      if ans == "exit":
        exit()
      if ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == num1 * num2:
        print(f"{Fore.GREEN}Correct")
        correct = correct + 1
      else:
        print(Fore.RED + "INCORRECT" + Fore.CYAN + "The correct answer was: " + str(num1*num2))
        incorrect = incorrect + 1
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print("Great work! Restart this app to do another mode!")
  elif mode == "d":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")

    if questions == 0:
      exit()

    correct = 0
    incorrect = 0
    
    for x in trange(int(questions)):
      num1 = random.randint(x + random.randint(1,x + 10), x + 20)
      num2 = random.randint(x + random.randint(1,x + 10), x + 20)
      print(f"{Fore.MAGENTA}What's {num1} ÷ {num2}? \n")
      ans = num1 / num2
      print(ans)
      if ans == "exit":
        exit()
      elif ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == round(num1 / num2, 2):
        correct = correct + 1
        print(Fore.GREEN + "Correct")
      else:
        incorrect = incorrect + 1
        print(Fore.RED + "INCORRECT" + Fore.CYAN + "The correct answer was: " + str(round(num1/num2, 2)))
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print(Fore.RED + "Great work! Restart this app to do another mode!")

  elif mode == "da":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")
    if questions == 0:
      exit()
    correct = 0
    incorrect = 0
    for x in trange(int(questions)):

      num1 = round(random.uniform(1, (x + 1)), 2)
      num2 = round(random.uniform(1, (x + 1)), 2)
      print(
        f"{Fore.MAGENTA}Whats {str(num1)} + {str(num2)}? {Fore.CYAN}\n")
      ans = num1 + num2
      print(ans)
      if ans == "exit":
        exit()
      if ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == num1 + num2:
        print(f"{Fore.GREEN}Correct")
        correct = correct + 1
      else:
        print(Fore.RED + "INCORRECT" + Fore.CYAN + "The correct answer was: " + str(num1+num2))
        incorrect = incorrect + 1
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print("Great work! Restart this app to do another mode!")
  elif mode == "ds":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    negative = input("Negative numbers? (y/n) \n")
    if negative == "y":
      positive = input("Positive numbers also? (y/n) \n")

    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")

    if questions == 0:
      exit()

    correct = 0
    incorrect = 0
    
    for x in trange(int(questions)):
      num1 = 0
      num2 = 0
      if negative == "y" and positive == "y":
        num1 = round(random.uniform(x * -1, x + 1), 2)
        num2 = round(random.uniform(x * -1, x + 1), 2)
      elif negative == "y" and positive == "n":
        num1 = round(random.uniform(x * -1, x * -1), 2)
        num2 = round(random.uniform(-x * -1, x * -1), 2)
      elif negative == "n":
        num1 = round(random.uniform(x, random.randint(x + 1, x + 20 )), 2)
        num2 = round(random.uniform(x, random.randint(x + 1, x + 20)), 2)
      print(f"{Fore.MAGENTA}What's {num1} - {num2}? \n")
      ans = num1 - num2
      print(ans)
      if ans == "exit":
        exit()
      elif ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == num1 - num2:
        correct = correct + 1
        print(Fore.GREEN + "Correct")
      else:
        incorrect = incorrect + 1
        print(Fore.RED + "INCORRECT" + Fore.CYAN + "The correct answer was: " + str(num1-num2))
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print(Fore.RED + "Great work! Restart this app to do another mode!")
  elif mode == "dm":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")
    if questions == 0:
      exit()
    correct = 0
    incorrect = 0
    for x in trange(int(questions)):

      num1 = round(random.uniform(1, (x + 1)), 2)
      num2 = round(random.uniform(1, (x + 1)), 2)
      print(
        f"{Fore.MAGENTA}Whats {str(num1)} x {str(num2)}? {Fore.CYAN}\n")
      ans = num1 * num2
      print(ans)
      if ans == "exit":
        exit()
      if ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == num1 * num2:
        print(f"{Fore.GREEN}Correct")
        correct = correct + 1
      else:
        print(f"{Fore.RED}INCORRECT {Fore.CYAN} The correct answer was: {num1 * num2}")
        incorrect = incorrect + 1
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print("Great work! Restart this app to do another mode!")
  elif mode == "dd":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")

    if questions == 0:
      exit()

    correct = 0
    incorrect = 0
    
    for x in trange(int(questions)):
      num1 = round(random.uniform(x + random.randint(1,x + 10), x + 20), 2)
      num2 = round(random.uniform(x + random.randint(1,x + 10), x + 20), 2)
      print(f"{Fore.MAGENTA}What's {num1} ÷ {num2}? \n")
      ans = num1 / num2
      print(ans)
      if ans == "exit":
        exit()
      elif ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"
      if convertable(ans) == False:
        ans = 0.00000001
        print("That's not a number. And if it's not a number then... Well it's wrong")
      if int(ans) == round(num1 / num2, 2):
        correct = correct + 1
        print(Fore.GREEN + "Correct")
      else:
        incorrect = incorrect + 1
        print(Fore.RED + "INCORRECT " + Fore.CYAN + "The correct answer was: " + str(round(num1/num2, 2)))
      print(Fore.CYAN + tabulate([[Fore.BLUE + str(x + 1), Fore.GREEN + str(correct), Fore.RED + str(incorrect) + Fore.CYAN]], headers=[Fore.BLUE + "Total", Fore.GREEN + "Correct", Fore.RED + "Incorrect" + Fore.CYAN], tablefmt="rounded_outline"))
    print(Fore.RED + "Great work! Restart this app to do another mode!")
 
