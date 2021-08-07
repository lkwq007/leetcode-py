class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # not correct
        cnt=0
        if len(nums)<3:
            return True
        leftmost=0
        for i in range(1,len(nums)):
            rightmost=nums[i+1] if i+1<len(nums) else 1001
            if nums[i]<=nums[i-1]:
                if leftmost<nums[i]<rightmost:
                    cnt+=1
                    nums[i-1]=leftmost
                elif (leftmost<nums[i-1]<rightmost):
                    cnt+=1
                    nums[i]=nums[i-1]
                    nums[i-1]=leftmost
                else:
                    return False
            leftmost=nums[i-1]
        return cnt<2