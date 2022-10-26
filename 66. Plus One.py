from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            digits[-2] == 1
            digits[-1] == 0
        else:
            digits[-1] += 1
        return digits


s = Solution()
print(s.plusOne([9]))
