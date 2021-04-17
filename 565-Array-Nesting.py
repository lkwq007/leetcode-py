class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # The elements of A are all distinct.
        ret=0
        for i in range(len(nums)):
            val=nums[i]
            nums[i]=-1
            acc=0
            while val>=0:
                acc+=1
                next=nums[val]
                nums[val]=-1
                val=next
            acc-=val
            acc-=1
            nums[i]=-acc
            ret=max(acc,ret)
        # print(nums)
        return ret