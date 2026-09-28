class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=set()
        for word in words:
            code=""
            for ch in word:
                index=ord(ch)-ord("a")
                code+=morse[index]
            result.add(code)
        return len(result)
        