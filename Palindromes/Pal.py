# Solver by mythers45#1807 on Discord

# Find an ideal value for a digit to make a target
def ideal(t):
  return max(t - 9, 0)

# Assign n to an index and its palindromic index
def ass(v, i, n):
  if(i == 0): # Case where nothing's on the ends
    return str(max(n, 0)) + v[1:len(v)-1] + str(max(n, 0))
  elif(i+1 == len(v)-i): # Case where nothing's in the middle
    return v[0:i] + str(max(n, 0)) + v[len(v)-i:len(v)]
  else: # Case where there are ends and a middle
    return v[0:i] + str(max(n, 0)) + v[i+1:len(v)-i-1]\
    + str(max(n, 0)) + v[len(v)-i:len(v)]

# Calculate an index of the first palindrome
# (+ set other palindromes to match up well)
def calc(l, i):
  d = l[0]
  if(i == 0):
    l[1] = ass(l[1], 0, int(d[0]) - 1)
    #print(l[1] + " " + l[2] + " " + l[3] + " i=" + str(i))

    while(not calc(l, 1)): # While next calc fails...
      # Increment value by 1 (if possible), retry
      l[1] = ass(l[1], 0, int(l[1][0]) + 1)
      if(l[1][0] > d[0]): # Final failure case: exit program
          print("Palindromes adding to " + d + " not found.")
          exit(2) # In theory, this should *never* happen
      #print(l[1] + " " + l[2] + " " + l[3] + " i=" + str(i))

  elif(i < 5):
    m = int(d[i]) + 9 # Main target (1 carry in, 1 carry out)
    if(i > 1): # Subtract third digit from target
      m -= int(l[3][i-2]) # (If there is one)
    if((i == 1 and l[1][0] == d[0]) or (i == 2 and\
    (int(l[1][1]) + int(l[2][0])) % 10 == int(d[1])) or (i > 2 and\
    (int(l[1][i-1]) + int(l[2][i-2]) + int(l[3][i-3])) % 10 == int(d[i-1]))):
        m -= 10 # Also subtract 10 if no carry out
    if(m < -1): # Failure case:
      return False # Can't go negative
    l[1] = ass(l[1], i, ideal(m))
    l[2] = ass(l[2], i - 1, max(m - int(l[1][i]), 0))
    s = int(d[-i]) - int(l[1][-i]) - int(l[2][-i])
    if(i > 1): # Secondary target- subtract carry in from this target
      s -= ((int(l[1][10-i:9]) + int(l[2][9-i:8])\
      + int(l[3][8-i:7])) // (10 ** (i - 1)))
    l[3] = ass(l[3], i - 1, s % 10)
    #print(l[1] + " " + l[2] + " " + l[3] + " i="
    #+ str(i) + " m=" + str(m) + " s=" + str(s))

    while(not calc(l, i + 1)): # While next calc fails...
      # Increment value by 1 (if possible), retry
      if(l[1][i] == "9"): # Special case: 1 over, no carry in
        if(int(l[1][i]) + int(l[2][i]) > m or l[2][i-1] == "9"):
          return False # Failure cases: can't go too far over
        l[2] = ass(l[2], i - 1, int(l[2][i-1]) + 1)
      else: # Normal case: increment and adjust
        l[1] = ass(l[1], i, int(l[1][i]) + 1)
        l[2] = ass(l[2], i - 1, m - int(l[1][i]))
        s = int(d[-i]) - int(l[1][-i]) - int(l[2][-i])
        if(i > 1): # Secondary target- subtract carry in from this target
          s -= ((int(l[1][10-i:9]) + int(l[2][9-i:8])\
          + int(l[3][8-i:7])) // (10 ** (i - 1)))
        l[3] = ass(l[3], i - 1, s % 10)
      #print(l[1] + " " + l[2] + " " + l[3] + " i="
      #+ str(i) + " m=" + str(m) + " s=" + str(s))

  # All slots set- verify sum and return all the way
  return (int(l[1]) + int(l[2]) + int(l[3])) % 1_000_000_000 == int(d)

# Input for calculation (must be an integer)
d = input("Enter a 9 digit number: ")
if(not(0 <= int(d) <= 999_999_999)):
  print("Invalid input")
  exit(1) # 0 to 999_999_999
for i in range(len(d), 9):
  d = "0" + d # Prepend 0s
l = [d, ".........", "........", "......."]
calc(l, 0) # Run full calculation and output if it returns here
print("Palindromes adding to " + d + " as follows:")
print(l[1] + " " + l[2] + " " + l[3])