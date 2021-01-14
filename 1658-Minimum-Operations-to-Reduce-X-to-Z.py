class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left=0
        acc=0
        # all numbers are postitive
        total=len(nums)
        if sum(nums)<x:
            return -1
        elif sum(nums)==x:
            return total
        left=0
        ret=total+1
        while left<total:
            acc+=nums[left]
            if acc==x:
                ret=left+1
                break
            elif acc>x:
                break
            left+=1
        if left==total:
            return -1
        right=len(nums)-1
        while right>left and left>=-1:
            tmp=nums[right]+acc
            if tmp>x and left>=0:
                acc-=nums[left]
                left-=1
            elif tmp==x:
                ret=min(ret,left+1+total-right)
                acc=tmp
                right-=1
            else:
                acc=tmp
                right-=1
        return ret if ret<total else -1