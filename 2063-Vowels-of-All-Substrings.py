class Solution:
    def countVowels(self, word: str) -> int:
        ret=0
        cur=0
        acc=0
        for item in word:
            if item in "aeiou":
                cur+=1
            acc+=cur
            ret+=acc
        return ret
