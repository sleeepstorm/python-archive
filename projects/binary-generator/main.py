import sys
import time
import random

def generate():
  st = ""
  for i in range(1000):
    e = random.randint(1, 2)
    if e == 1:
      st += "0"
    else:
      st += "1"
  return st

words = generate()
for char in words:
    time.sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
