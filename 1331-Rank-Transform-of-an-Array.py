class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        record={}
        for item in arr:
            record[item]=1
        keys=list(record.keys())
        idx=1
        for key in sorted(keys):
            record[key]=idx
            idx+=1
        return [record[item] for item in arr]