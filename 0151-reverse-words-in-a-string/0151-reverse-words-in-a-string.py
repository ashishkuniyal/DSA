class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        ans=""
        s=s[::-1]
        i=0
        while i<n:
            word=""
            while i<n and s[i]!=" ":
                word+=s[i]
                i+=1
            word=word[::-1]
            if len(word)>0:
                ans+=" "+word
            i+=1
        return ans[1:]
        