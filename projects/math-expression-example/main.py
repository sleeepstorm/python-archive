import requests
from urllib import parse
input = input("Enter a math problem: \n > ")

input = input.replace("x", "*")

URL = "http://api.mathjs.org/v4/?expr=" + parse.quote(input)


r = requests.get(url = URL)

data = r.json()

print(data)
