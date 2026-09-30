class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        ans=0
        for sentence in sentences:
            word=len(sentence.split())
            if word > ans:
                ans=word
        return ans
  