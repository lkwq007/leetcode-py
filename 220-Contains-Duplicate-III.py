class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums)<=k:
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i+1]-nums[i]<=t:
                    return True
            return False
        for i in range(k+1,len(nums)+1):
            lst=nums[i-k-1:i]
            lst.sort()
            for j in range(k):
                if lst[j+1]-lst[j]<=t:
                    return True
        return False

# wrong
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        lst=[(nums[idx],idx) for idx in range(len(nums))]
        lst.sort()
        start=0
        while start<len(nums):
            idx=start
            while idx<len(nums) and lst[start][0]+t>=lst[idx][0]:
                if abs(lst[start][1]-lst[idx][1])<=k:
                    return True
                idx+=1
            start+=1
        return False