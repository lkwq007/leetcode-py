class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ret=0
        total=0
        acc=1
        start=-1
        first=-1
        last=0
        for i in range(len(nums)):
            if nums[i]==0:
                if acc>0:
                    ret=max(total,ret)
                else:
                    ret=max(ret,first-1,total-first,last-1,total-last)
                start=i
                acc=1
                total=0
                first=-1
                last=0
            else:
                total+=1
                acc=acc*(1 if nums[i]>0 else -1)
                if nums[i]<0:
                    if first==-1:
                        first=i-start
                    last=0
                last+=1
        if acc>0:
            ret=max(total,ret)
        else:
            ret=max(ret,first-1,total-first,last-1,total-last)
        return ret