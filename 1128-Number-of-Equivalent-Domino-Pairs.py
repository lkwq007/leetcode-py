class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        record=[0]*100
        for a,b in dominoes:
            record[max(a,b)*10+min(a,b)]+=1
        ret=0
        for item in record:
            if item>1:
                ret+=item*(item-1)//2
        return ret

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        record=[0]*100
        ret=0
        for a,b in dominoes:
            idx=min(a,b)*10+max(a,b)
            ret+=record[idx]
            record[idx]+=1
        return ret