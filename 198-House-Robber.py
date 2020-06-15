class Solution:
    def rob(self, nums: List[int]) -> int:
        last,now=0,0
        for item in nums:
            last,now=now,max(last+item,now)
        return now
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        if len(nums)<3:
            return max(nums)
        if nums[0]>nums[1]:
            first=0
            second=1
        else:
            first=1
            second=0
        for idx in range(2,len(nums)):
            if (idx-1)==first:
                nums[idx]+=nums[second]
            else:
                nums[idx]+=nums[first]
            if nums[idx]>nums[first]:
                second=first
                first=idx
            elif nums[idx]>nums[second]:
                second=idx
        return nums[first]