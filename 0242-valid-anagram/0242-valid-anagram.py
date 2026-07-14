class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram=sorted(s)
        aanagram=sorted(t)
        if anagram==aanagram:
            return True
        else:
            return False
        