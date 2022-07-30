class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        record={}
        record[0]=1
        acc=0
        ret=0
        for item in nums:
            acc+=item
            target=acc-goal
            ret+=record.get(target,0)
            record[acc]=record.get(acc,0)+1
        return ret

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        record=[0]*30001
        record[0]=1
        acc=0
        ret=0
        for item in nums:
            acc+=item
            target=acc-goal
            ret+=record[target]
            record[acc]+=1
        return ret
