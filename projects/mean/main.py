from art import text2art
from colorama import Fore

print(text2art("mean", font='3d_diagonal'))
print(text2art("by nikhilhex", font='bell'))

length = input(Fore.MAGENTA + "Enter length of list \n")

values = []

for x in range(int(length) + 1):
  if x != 0:
    tmp = input(str(x) + ") ")
    values.append(int(tmp))
    
print(f"{Fore.CYAN}The mean, or average of the given numbers is {round(sum(values) / len(values), 2)}")
