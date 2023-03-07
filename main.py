nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]
target = 10



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
            
    


ratkaisu = Solution()
ratkaisu.twoSum(nums, target)

