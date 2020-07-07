class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=(1+n)*n//2
        return total-sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # no over flow
        acc=0
        for i in range(len(nums)):
            acc+=i+1-nums[i]
        return acc

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        acc=len(nums)
        for i in range(len(nums)):
            acc^=i^nums[i]
        return acc