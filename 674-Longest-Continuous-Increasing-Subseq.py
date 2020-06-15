from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest=1
        idx=0
        total=len(nums)-1
        if total<0:
            return 0
        start=0
        end=0
        while idx<total:
            if nums[idx+1]<=nums[idx]:
                start=idx+1
                end=idx+1
            else:
                end=idx+1
            if end-start+1>longest:
                longest=end-start+1
            idx+=1
        return longest

x=Solution()
print(x.findLengthOfLCIS([1]))
print(x.findLengthOfLCIS([1,2,3]))
print(x.findLengthOfLCIS([1,1,1]))