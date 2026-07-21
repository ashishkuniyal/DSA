class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        ones=0
        section=[]
        i=0
        while i<n:
            if s[i]=='0':
                j=i
                while j<n and s[j]==s[i]: j+=1
                section.append(j-i)
                i=j
            else:
                ones+=1
                i+=1
        if len(section)<2: return ones
        best=0
        for i in range(1,len(section)):
            best=max(best,section[i]+section[i-1])
        return ones+best