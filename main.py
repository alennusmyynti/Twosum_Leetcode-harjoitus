nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]
target = 10

printtext = 0
#indicates whether or not the system prints text


class Solution:

  def __init__(self):
    self.nums = []
    self.target = 0
    self.total = 0

  def twoSum(self, lukujono, tavoite):
    self.nums = lukujono
    self.target = tavoite

    for x in range(len(self.nums)):

      for y in range(len(self.nums)):
        if y > x:
          if self.nums[x] + self.nums[y] == target:

            print([x, y])
            if printtext == 1:
              print(self.nums[x], "+", self.nums[y], "=", self.target)
              self.total += 1

              print("")

    if printtext == 1:
      print("")
      print("Total:", self.total)


if printtext == 1:
  print("Solutions:")
  print("")

ratkaisu = Solution()
ratkaisu.twoSum(nums, target)
if printtext == 1:
  print("")
  print("------------------------------------------------")
  print("")
  print("Used Values:")
  for z in range(len(nums)):

    print(z, " - ", nums[z])

  print("")
  print("Two-Sum Target:")
  print(ratkaisu.target)

  print("")
  print("Credit: eelis")
