class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even=0
        odd=0
        for i in range(len(nums)):
            if i&1:
                odd+=nums[i]
            else:
                even+=nums[i]
        head_even=0
        head_odd=0
        ret=0
        for i in range(len(nums)):
            if i&1:
                odd-=nums[i]
            else:
                even-=nums[i]
            if head_even+odd==head_odd+even:
                ret+=1
            if i&1:
                head_odd+=nums[i]
            else:
                head_even+=nums[i]
        return ret
            