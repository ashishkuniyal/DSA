class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i ,ch in enumerate(s,1):
            reverse=26-(ord(ch)-ord('a'))
            total+=reverse*i
        return total
        