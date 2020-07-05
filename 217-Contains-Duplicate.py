class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record={}
        for item in nums:
            if item in record:
                return True
            else:
                record[item]=1
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(len(nums)-1):
            if nums[idx]==nums[idx+1]:
                return True
        return False