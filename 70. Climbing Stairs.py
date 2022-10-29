class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

    # O(1) solution with math
    def faster(self, n: int) -> int:
        import math
        gold = (1 + math.sqrt(5))/2

        ans = ((gold ** n) - ((1 - (gold)) ** n)) // math.sqrt(5)
        print(ans)
        return int(ans)


s = Solution()
print(s.climbStairs(3))