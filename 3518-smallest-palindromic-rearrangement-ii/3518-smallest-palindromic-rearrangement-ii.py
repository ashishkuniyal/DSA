class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
from math import comb

class Solution:
    LIMIT = 10 ** 6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, f in freq.items():
            half[ord(ch) - 97] = f // 2
            if f & 1:
                mid = ch

        if self.countWays(half) < k:
            return ""

        left = []
        m = sum(half)

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(i + 97))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def countWays(self, cnt):
        total = sum(cnt)
        ans = 1

        for x in cnt:
            if x:
                ans *= comb(total, x)
                if ans >= self.LIMIT:
                    return self.LIMIT
                total -= x

        return ans
        