class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        record={}        
        for item in nums:
            if item>0:
                record[item]=1
        return len(record)