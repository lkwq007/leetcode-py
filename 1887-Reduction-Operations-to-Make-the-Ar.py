class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ret=0
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:-x)
        acc=0
        for i in range(len(keys)-1):
            acc+=record[keys[i]]
            ret+=acc
        return ret