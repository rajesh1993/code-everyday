def printZigZag(word, k):
  topSpace = 2 * k - 2
  i = 0
  for row in range(k):
    space = 0
    while space < i:
        print(" ", end = "")
        space += 1
    invert = False
    j = row
    while j < len(word):
      print(word[j], end = "")
      if row > 0 and row < k - 1:
        if not invert:
          countSpaces = topSpace - (2 * row)
        else:
          countSpaces = topSpace - (2 * (k - row - 1))
      else:
        countSpaces = topSpace
      print(''.join([" " for z in range(countSpaces - 1)]), end = "")
      j += countSpaces
      invert = not invert
    print()
    i += 1

      

printZigZag("abcdefghijklmnopqrst", 8)