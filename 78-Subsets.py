class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<1:
            return []
        ret=[]
        # assume that len(nums) is not large
        total=2**len(nums)
        for idx in range(total):
            tmp=[]
            pos=0
            while idx>0:
                if idx&1:
                    tmp.append(nums[pos])
                pos+=1
                idx=idx>>1
            ret.append(tmp)
        return ret