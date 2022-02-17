class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst=[[],[]]
        for item in nums:
            idx=0 if item>0 else 1
            lst[idx].append(item)
        for i in range(len(nums)):
            nums[i]=lst[i%2][i//2]
        return nums