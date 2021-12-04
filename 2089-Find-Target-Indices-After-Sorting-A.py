class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ret=[]
        for i in range(len(nums)):
            if nums[i]==target:
                ret.append(i)
        return ret

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst=[0]*102
        for item in nums:
            lst[item]+=1
        if lst[target]==0:
            return []
        acc=0
        for i in range(target):
            acc+=lst[i]
        return list(range(acc,acc+lst[target]))