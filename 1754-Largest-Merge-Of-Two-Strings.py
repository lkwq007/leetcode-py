class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        idx1=0
        idx2=0
        ret=[]
        while idx1<len(word1) and idx2<len(word2):
            if word1[idx1]>word2[idx2]:
                ret.append(word1[idx1])
                idx1+=1
            elif word1[idx1]<word2[idx2]:
                ret.append(word2[idx2])
                idx2+=1
            elif word1[idx1:]>word2[idx2:]:
                ret.append(word1[idx1])
                idx1+=1

        idx,word=(idx1,word1) if idx1<len(word1) else (idx2,word2)
        while idx<len(word):
            ret.append(word[idx])
            idx+=1
        return "".join(ret)