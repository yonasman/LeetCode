class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      output = []

      for n in nums:
        count = 0
        for m in nums:
          if(n > m):
             count += 1
        output.append(count)
      return output