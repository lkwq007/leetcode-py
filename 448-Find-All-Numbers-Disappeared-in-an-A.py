class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret=[]
        for idx in range(len(nums)):
            item=abs(nums[idx])-1
            nums[item]=-abs(nums[item])
        for idx in range(len(nums)):
            if nums[idx]>0:
                ret.append(idx+1)
        return ret
