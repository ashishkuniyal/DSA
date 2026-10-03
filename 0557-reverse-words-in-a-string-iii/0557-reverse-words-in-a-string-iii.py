class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        result=[]
        for word in words:
            reverse_word=word[::-1]
            result.append(reverse_word)
        return " ".join(result)
        