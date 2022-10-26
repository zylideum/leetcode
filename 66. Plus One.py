from typing import List


class Solution:
    # Abuses the ease of Python type assignments
    # Leetcode shouldn't accept this since it returns
    # an array of strings despite the type annotation
    def plusOne(self, digits: List[int]) -> List[int]:
        buildStr = ""
        for num in digits:
            buildStr += str(num)

        buildStr = int(buildStr) + 1

        return list(str(buildStr))

    def neetCode(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else: 
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]


s = Solution()
print(s.plusOne([1, 0, 9]))
print(s.neetCode([1, 0, 9]))
