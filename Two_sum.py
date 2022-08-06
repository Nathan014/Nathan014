from itertools import combinations
def twoSum(nums, target):
    combi = list(combinations(nums, 2))
    for i in combi:
        if sum(i) == target:
            return i
while True:
  try:
    length = int(input("Input the length of array: "))
    break
  except ValueError:
    print("Please enter a number")
count = 0
list_nums = []
while count < length:
  try:
    list_nums.append(int(input()))
  except ValueError:
    print("Please enter a number")
    continue
  count += 1
while True:
  try:
    target_input = int(input("Input the target: "))
    break
  except ValueError:
    print("Please enter a number")
print(twoSum(list_nums, target_input))
