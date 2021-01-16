class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:-x)
        return nums[k-1]