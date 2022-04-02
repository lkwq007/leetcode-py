class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        record=[0]*26
        for item in word1:
            record[ord(item)-ord("a")]+=1
        for item in word2:
            record[ord(item)-ord("a")]-=1
        for i in range(26):
            if record[i]<-3 or record[i]>3:
                return False
        return True