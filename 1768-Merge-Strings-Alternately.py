class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret=[]
        for a,b in zip(word1,word2):
            ret.append(a)
            ret.append(b)
        word,idx=(word2,len(word1)) if len(word1)<len(word2) else (word1,len(word2))
        while idx<len(word):
            ret.append(word[idx])
            idx+=1
        return "".join(ret)