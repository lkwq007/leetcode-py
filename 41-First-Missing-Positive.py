class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        total=len(nums)
        for i in range(len(nums)):
            if nums[i]<1:
                nums[i]=
        for i in range(len(nums)):
            cur=nums[i]
            if cur>0:
                nums[i]=0
                if cur<=total:
                    pos=cur-1
                    next=nums[pos]
                    while 0<next<=total:
                        nums[pos]=-1
                        pos=next-1
                        next=nums[pos]
                    nums[pos]=-1
        for i in range(len(nums)):
            if nums[i]!=-1:
                return i+1
        return total+1