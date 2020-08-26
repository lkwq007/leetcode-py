class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        record={}
        for item in words:
            record[item]=record.get(item,0)+1
        return map(lambda x:x[1],sorted([(-val,key) for key,val in record.items()])[:k])