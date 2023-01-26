class Solution:
    def similarPairs(self, words: List[str]) -> int:
        record={}
        for item in words:
            tmp=frozenset(item)
            record[tmp]=record.get(tmp,0)+1
        ret=0
        for k,v in record.items():
            ret+=v*(v-1)//2
        return ret