class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue=[]
        max_queue=[]
        