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


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        record={}
        start={}
        lst=set(list("aeiou"))
        ret=0
        last=0
        for i,item in enumerate(word):
            if item in lst:
                record[item]=i
                if item not in start:
                    start[item]=i
                if len(start)==5:
                    last=min(record.values())-min(start.values())+1
                ret+=last
            else:
                record={}
                start={}
                last=0
        return ret