class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lst=sorted(nums)
        i=0
        while i<len(nums) and nums[i]==lst[i]:
            i+=1
        left=i
        i=len(nums)-1
        while i>=0 and nums[i]==lst[i]:
            i-=1
        right=i
        if right<=left:
            return 0
        return right-left+1