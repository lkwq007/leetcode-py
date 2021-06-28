class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 0-based indexing
        odd=0
        even=0
        for item in nums:
            even,odd=max(even,odd+item),max(odd,even-item)
        return max(even,odd)