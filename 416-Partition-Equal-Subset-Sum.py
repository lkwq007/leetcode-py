class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        for item in nums:
            total+=item
        if total%2==1:
            return False
        half=total//2
        for item in nums:
            if item>half:
                return False
        return True