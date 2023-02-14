class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ret=0
        for i in range((len(nums)+1)//2):
            if i==len(nums)-i-1:
                ret+=nums[i]
            else:
                ret+=int(str(nums[i])+str(nums[len(nums)-i-1]))
        return ret