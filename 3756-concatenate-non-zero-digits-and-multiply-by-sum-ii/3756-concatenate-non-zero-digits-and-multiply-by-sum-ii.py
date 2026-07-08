from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        positions = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                positions.append(i)
                digits.append(int(ch))

        n = len(digits)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated value
        H = [0] * (n + 1)
        for i in range(n):
            H[i + 1] = (H[i] * 10 + digits[i]) % MOD

        # prefix digit sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(positions, l)
            right = bisect_right(positions, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (H[right + 1] - H[left] * pow10[length]) % MOD
            digit_sum = prefix[right + 1] - prefix[left]

            ans.append((x * digit_sum) % MOD)

        return ans