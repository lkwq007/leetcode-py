class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        record={}
        ret=[]
        for item in A.split(" "):
            record[item]=record.get(item,0)+1
        for item in B.split(" "):
            if item in record:
                record[item]=0
            else:
                record[item]=1
        for key,val in record.items():
            if val==1:
                ret.append(key)
        return ret