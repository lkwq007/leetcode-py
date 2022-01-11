class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        record={}
        mapping={}
        mask=1
        for i in range(26):
            mapping[chr(ord("a")+i)]=mask
            mask=mask<<1
        for word in startWords:
            acc=0
            for item in word:
                acc=acc|mapping[item]
            record[acc]=1
        ret=0
        for word in targetWords:
            acc=0
            for item in word:
                acc=acc|mapping[item]
            for item in word:
                cur=acc^mapping[item]
                if cur in record:
                    ret+=1
                    break
        return ret