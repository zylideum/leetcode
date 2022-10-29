from re import L
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        while (m > 0 and n > 0):
            if nums2[n - 1] > nums1[m - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1
        
        while (n > 0):
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

        print(nums1)
s = Solution()
s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)