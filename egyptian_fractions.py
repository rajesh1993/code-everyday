# Egyptian fractions

def egyptianFractions(nr, dr):
  if nr % dr == 0:
    print(nr / dr)
    return
  if dr % nr == 0:
    print("1/%d" % (dr//nr))
    return
  ceil = dr // nr + 1
  print("1/%d + " % ceil, end = "")
  egyptianFractions(nr * ceil - dr, dr * ceil)

# Test Cases
egyptianFractions(9, 20)