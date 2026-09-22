class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum=max(candies)
        result=[]
        for candy in candies:
            result.append(candy+extraCandies>=maximum)
        return result
        
        