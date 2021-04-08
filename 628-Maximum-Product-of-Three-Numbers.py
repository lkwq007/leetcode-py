class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1]<1:
            return nums[-1]*nums[-2]*nums[-3]
        left=nums[0]*nums[1]
        right=nums[-1]*nums[-2]
        return max(left*nums[-1],right*nums[-3])
