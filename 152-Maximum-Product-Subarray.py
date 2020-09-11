class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        ret=nums[0]
        acc=None
        start=-1
        def compute(start,end,acc,ret):
            i=end
            if i-2==start:
                return max(ret,nums[i-1])
            idx=i-1
            postfix=1
            prefix=1
            while idx>start and nums[idx]>0:
                postfix*=nums[idx]
                idx-=1
            right=nums[idx]
            idx=start+1
            while idx<i and nums[idx]>0:
                prefix*=nums[idx]
                idx+=1
            left=nums[idx]
            ret=max(ret,0,prefix if idx!=start+1 else 0,postfix if idx!=i-1 else 0,acc//left//prefix,acc//right//postfix)
            return ret
        for i in range(len(nums)):
            if nums[i]==0:
                ret=max(0,ret)
                if acc is None:
                    start=i
                    continue
                if acc>0:
                    ret=max(ret,acc)
                else:
                    ret=compute(start,i,acc,ret)
                acc=None
                start=i
            else:
                if acc is None:
                    acc=nums[i]
                else:
                    acc*=nums[i]
        if acc is not None:
            if acc>0:
                ret=max(ret,acc)
            else:
                ret=compute(start,len(nums),acc,ret)
        return ret