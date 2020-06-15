class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret=[]
        for idx in range(0,len(nums),2):
            for i in range(0,nums[idx]):
                ret.append(nums[idx+1])
        return ret