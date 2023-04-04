class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort(reversed=True)
        idx1=0
        idx2=0
        ret=0
        while idx1<len(nums) and idx2<len(nums):
            if nums[idx1]==0:
                idx1+=1
                continue
            if nums[idx2]2*nums[idx1]:
                idx2+=1
            else:
                nums[idx2]=0
                nums[idx1]=0
                idx2+=1
                idx1+=1
                ret+=2
        return ret