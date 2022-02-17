class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones=sum(nums)
        zeros=len(nums)-ones
        acc0=0
        acc1=0
        ret=ones
        lst=[0]
        for i in range(len(nums)):
            acc1+=nums[i]
            acc0=i+1-acc1
            cur=acc0+ones-acc1
            if cur>ret:
                ret=cur
                lst=[i+1]
            elif cur==ret:
                lst.append(i+1)
        return lst            