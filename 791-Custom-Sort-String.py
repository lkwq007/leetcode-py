class Solution:
    def customSortString(self, S: str, T: str) -> str:
        record={}
        for item in T:
            record[item]=record.get(item,0)+1
        ret=""
        for item in S:
            if item in record:
                ret+=item*record[item]
                del record[item]
        for key,val in record.items():
            ret+=key*val
        return ret