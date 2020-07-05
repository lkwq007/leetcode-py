class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record={}
        for idx in range(len(nums)):
            item=nums[idx]
            if item in record and idx-record[item]<=k:
                return True
            record[item]=idx
        return False