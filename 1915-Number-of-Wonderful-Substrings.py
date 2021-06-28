class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        record={0:1}
        base=ord("a")
        mapping={0:0}
        ret=0
        acc=0
        mask=1
        for i in range(10):
            mapping[chr(base+i)]=mask
            mapping[i+1]=mask
            mask=mask<<1
        for i in range(len(word)):
            val=mapping[word[i]]
            acc=val^acc
            for i in range(11):
                ret+=record.get(acc^mapping[i],0)
            record[acc]=record.get(acc,0)+1
        return ret