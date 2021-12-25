class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lst=[(-nums[i],i) for i in range(len(nums))]
        lst.sort()
        lst=lst[:k]
        lst.sort(key=lambda x:x[1])
        return [-item[0] for item in lst]