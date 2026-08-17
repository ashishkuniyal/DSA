class Solution:
    def arrangeCoins(self, n: int) -> int:
        row=1
        count=0
        while n>=row:
            n-=row
            count+=1
            row+=1
        return count