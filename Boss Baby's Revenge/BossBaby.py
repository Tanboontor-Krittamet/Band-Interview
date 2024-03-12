def boss_baby():
  """
  Simulates Boss Baby judging kids based on "S" and "R" characters.
  """
  print("---------- Boss Baby's Revenge ----------")

  # Array of strings representing kid's behavior
  arr = ["SRSSRRR", "RSSRR", "SSSRRRRS", "SSRR", "SRRSSR"]

  for string in arr:
    # Split string into a list of characters
    chars = list(string)
    rev = 0  # Keep track of "good" points

    print(f"Input: {string}")

    for char in chars:
      # Check for "R" at the beginning
      if char == "R" and chars.index(char) == 0:
        rev += 1
        break

      # Count "S" and decrease for "R" (except starting "R")
      if char == "S":
        rev += 1
      elif char == "R":
        rev -= 1

      # Ensure rev doesn't go below 0
      rev = max(rev, 0)

    # Determine verdict
    if rev > 0:
      print("Output:", "Bad Boy")
    else:
      print("Output:", "Good Boy")

  print("---------- Boss Baby's Revenge ----------")

if __name__ == "__main__":
  boss_baby()
