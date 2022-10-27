from xml.dom import minidom


class Solution:
    def mySqrt(self, x: int) -> int:
        # Halved Method, Slow. Technically O(1/2N)? Drop the constant
        if x == 1:
            return 1
        searchLen = x // 2
        i = 1
        possible = [0]
        while i <= searchLen:
            if (i * i) <= x:
                possible[0] = i
                i += 1
            else:
                break

        return possible[0]

    def binarySearch(self, x: int) -> int:
        # Binary Search Method, Faster but doesn't work for 8??
        if x < 2:
            return x

        ans = 0
        lower = 1
        upper = x // 2

        while lower <= upper:
            tar = (lower + upper) // 2
            sqr = tar * tar

            if sqr == x:
                return tar
            elif sqr < x:
                lower = tar + 1
                ans = tar
            else:
                upper = tar - 1
        return ans


s = Solution()
print(s.binarySearch(8))
