from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        mx = [0] * n
        pgcd = [0] * n

        mx[0] = nums[0]
        pgcd[0] = nums[0]

        for i in range(1, n):
            mx[i] = max(mx[i - 1], nums[i])   # Fixed
            pgcd[i] = gcd(nums[i], mx[i])

        pgcd.sort()

        res = 0
        for i in range(n // 2):
            res += gcd(pgcd[i], pgcd[n - 1 - i])

        return res

        