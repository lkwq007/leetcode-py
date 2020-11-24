class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # brute force
        return "".join(word1)=="".join(word2)

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # [TODO] inplace, need revising
        i1,i2=0,0
        j1,j2=0,0
        total1=0
        total2=0
        for item in word1:
            total1+=len(item)
        for item in word2:
            total2+=len(item)
        if total1!=total2:
            return False
        while i1<len(word1) and i2<len(word2):
            while j1<len(word1[i1]) and j2<len(word2[i2]):
                if word1[i1][j1]!=word2[i2][j2]:
                    return False
                j1+=1
                j2+=1
            if j1>=len(word1[i1]):
                i1+=1
                j1=0
            if j2>=len(word2[i2]):
                i2+=1
                j2=0
        return True
