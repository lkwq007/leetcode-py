class Solution:
    def frequencySort(self, s: str) -> str:
        record={}
        for item in s:
            if item in record:
                record[item]+=1
            else:
                record[item]=1
        lst=list(record.keys())
        lst.sort(key=lambda x:-record[x])
        ret=""
        for item in lst:
            if record[item]>0:
                ret+=item*record[item]
        return ret
