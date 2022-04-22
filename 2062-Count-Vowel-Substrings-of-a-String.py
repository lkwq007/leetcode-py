class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # brute force, not good
        ret=0
        mapping={}
        lst=list("aeiou")
        mask=1
        for i in range(5):
            mapping[lst[i]]=mask
            mask=mask<<1
        full=mask-1
        for i in range(len(word)):
            for j in range(i,len(word)):
                acc=0
                for k in range(i,j+1):
                    if word[k] not in "aeiou":
                        acc=0
                        break
                    else:
                        acc|=mapping[word[k]]
                if acc&full==full:
                    ret+=1
        return ret
