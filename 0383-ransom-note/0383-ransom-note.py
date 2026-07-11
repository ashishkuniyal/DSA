class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter={}
        for c in magazine:
            if c not in letter:
                letter[c]=1
            else:
                letter[c]+=1
        for c in ransomNote:
            if c not in letter:
                return False
            if letter[c]==0:
                return False
            letter[c]-=1
        return True
        