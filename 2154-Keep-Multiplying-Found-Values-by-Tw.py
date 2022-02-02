class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        record=[0]*2001
        for item in nums:
            record[item]=1
        while record[original]:
            original*=2
        return original