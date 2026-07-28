class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        mid=n//2
        s=list(s)
        s[:mid]=sorted(s[:mid])
        for i in range(mid):
            s[n-1-i]=s[i]
        return "".join(s)
     
        