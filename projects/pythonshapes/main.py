# Used to color UI
from colorama import Fore, Back, Style

# Used for sleep()
import time

#  Used to clear console
import os

# Values used in UI
backColor = Back.WHITE
foreDash1 = Fore.RED
lineSep1 = Fore.GREEN
foreDash2 = Fore.BLUE
lineSep2 = Fore.RED
foreDash3 = Fore.YELLOW
lineSep3 = Fore.WHITE
plus = Fore.BLUE
wall1 = Fore.RED
wall2 = Fore.BLUE

# Number
nums = 0

# Spaces (the more numbers added the more this shifts over so this is added to prevent that from happening)
spaces = "                       "

# Design
frame = f"""
{plus}+{foreDash1}--{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}----{plus}+
{wall1}|{backColor}                                               {Back.RESET}|
{wall2}|{backColor}                       {nums}                       {Back.RESET}|
{wall1}|{backColor}                                               {Back.RESET}|
{wall2}|{backColor}                                               {Back.RESET}|
{wall1}|{backColor}                                               {Back.RESET}|
{wall2}|{backColor}                                               {Back.RESET}|
{wall1}|{backColor}                                               {Back.RESET}|
{wall2}|{backColor}                                               {Back.RESET}|
{wall1}|{backColor}                                               {Back.RESET}|
{wall2}|{backColor}                                               {Back.RESET}|
{plus}+{foreDash1}--{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}----{plus}+
"""

def updateFrame():
  global nums
  global spaces
  nums += 1
  prevDigit = len(str(nums))
  if nums == 10:
    spaces = spaces[:-1]
  if nums == 100:
    spaces = spaces[:-1]
  
  frame = f"""
  {plus}+{foreDash1}--{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}----{plus}+
  {wall1}|{backColor}                                               {Back.RESET}|
  {wall2}|{backColor}                       {nums}{spaces}{Back.RESET}|
  {wall1}|{backColor}                                               {Back.RESET}|
  {wall2}|{backColor}                                               {Back.RESET}|
  {wall1}|{backColor}                                               {Back.RESET}|
  {wall2}|{backColor}                                               {Back.RESET}|
  {wall1}|{backColor}                                               {Back.RESET}|
  {wall2}|{backColor}                                               {Back.RESET}|
  {wall1}|{backColor}                                               {Back.RESET}|
  {wall2}|{backColor}                                               {Back.RESET}|
  {plus}+{foreDash1}--{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}---{lineSep3}|{foreDash1}---{lineSep1}|{foreDash2}---{lineSep2}|{foreDash3}----{plus}+
  """
  os.system("clear")
  print(frame)
  time.sleep(1)
  updateFrame()

updateFrame()
