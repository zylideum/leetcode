from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in elements:
                return [elements[difference], i]
            elements[n] = i


s = Solution()
print(s.twoSum([1, 2, 4, 5, 5], 10))