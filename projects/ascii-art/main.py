from art import text2art
from colorama import Fore

print(Fore.RED + "Welcome to land of the ascii art")
print(Fore.BLUE + "The font is random. If you don't like it than restart the project. maybe you will find a font you like?")
text = input(f"{Fore.GREEN}What's the text \n {Fore.YELLOW}> ")

print(Fore.WHITE + text2art(text,"random"))
