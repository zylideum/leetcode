from typing import List


class Solution:
    # My solution, where there is 1 pointer that compares to the next value
    #  and removes in-place then moves to the next value
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        while (x < len(nums) - 1):
            if (nums[x] == nums[x + 1]):
                del nums[x]
            else:
                x += 1

        return x + 1, nums

    # Easy Python Solution abusing set
    def testdup(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        return len(nums), nums


s = Solution()
ints = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.testdup(ints))
