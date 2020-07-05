class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        lst=[(nums[idx],idx) for idx in range(len(nums))]
        lst.sort()
        for idx in range(len(nums)-1):
            if abs(lst[idx][0]-lst[idx+1][0])<=t and abs(lst[idx][1]-lst[idx+1][1])<=k:
                return True
        return False      