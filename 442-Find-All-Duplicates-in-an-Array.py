class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # len(nums)=n, 1<=nums[i]<=n
        ret=[]
        for idx in range(len(nums)):
            item=abs(nums[idx])-1
            if nums[item]<0:
                ret.append(item+1)
            else:
                nums[item]=-nums[item]
        return ret
