from colorama import Back, Fore

def generateSquare(width, height, topPattern, bottomPattern, leftWallPattern, rightWallPattern, tlEdge, trEdge, blEdge, brEdge, borderColor, boxColor):
  lw = ""
  for x in range(height):
    lw += leftWallPattern + boxColor + (" " * len(topPattern * width)) + Back.RESET +  rightWallPattern + "\n" 
  frame = f"""
{borderColor}{tlEdge}{topPattern * width}{trEdge}
{lw}{blEdge}{bottomPattern * width}{brEdge}
  """
  return frame


print(generateSquare(10, 20, "-=-", "-+-", "|-", "-|", "+", "+", "+", "+", Fore.RED, Back.WHITE))
