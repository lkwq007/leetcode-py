class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ret=set()
        for i in range(len(nums)):
            if nums[i]==key:
                for j in range(i-k,i+k+1):
                    if j>=0 and j<len(nums):
                        ret.add(j)
        ret=list(ret)
        ret.sort()
        return ret