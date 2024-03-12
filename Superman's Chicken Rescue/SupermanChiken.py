def superman_chicken():
  print("---------- Superman's Chicken Rescue ----------")

  # Example 1
  area1 = 5
  chickens1 = [2, 5, 10, 12, 15]
  print("Example 1")
  print("Rescue Chicken Number:", rescue(area1, chickens1))

  # Example 2
  area2 = 10
  chickens2 = [1, 11, 30, 34, 35, 37]
  print("Example 2")
  print("Rescue Chicken Number:", rescue(area2, chickens2))
  print("---------- Superman's Chicken Rescue ----------")

def rescue(roof, chickens):
  num_rescued = 0
  for i in range(len(chickens)):
    reach = chickens[i] + roof - 1
    count = 1
    for j in range(i + 1, len(chickens)):
      if reach >= chickens[j]:
        count += 1
      else:
        break
    if count > num_rescued:
      num_rescued = count
  return num_rescued

if __name__ == "__main__":
  superman_chicken()
