class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ret=0
        record={}
        for item in words1:
            record[item]=record.get(item,0)+1
        keys=[k for k,v in record.items() if v==1]
        record={}
        for item in words2:
            record[item]=record.get(item,0)+1
        ret=0
        for k in keys:
            if record.get(k,0)==1:
                ret+=1
        return ret