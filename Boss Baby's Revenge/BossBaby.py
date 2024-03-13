def boss_baby():
  print("---------- Boss Baby's Revenge ----------")

  # Example
  arr = ["SRSSRRR", "RSSRR", "SSSRRRRS", "SSRR", "SRRSSR"]

  for string in arr:
    chars = list(string)
    rev = 0

    print(f"Input: {string}")

    for char in chars:
      if char == "R" and chars.index(char) == 0:
        rev += 1
        break

      if char == "S":
        rev += 1
      elif char == "R":
        rev -= 1

      rev = max(rev, 0)

    if rev > 0:
      print("Output:", "Bad Boy")
    else:
      print("Output:", "Good Boy")

  print("---------- Boss Baby's Revenge ----------")

if __name__ == "__main__":
  boss_baby()
