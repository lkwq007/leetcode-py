class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret=sum(nums[:3])
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                cur=nums[i]+nums[j]
                tgt=target-cur
                left=j+1
                right=len(nums)-1
                while left<right:
                    middle=left+(right-left)//2
                    if nums[middle]==tgt:
                        return target
                    elif nums[middle]<tgt:
                        left=middle+1
                    else:
                        right=middle
                lst=[(left-1) if left-1!=j else left,left,(left+1) if (left+1)<len(nums) else left]
                for idx in lst:
                    tmp=cur+nums[idx]
                    if abs(ret-target)>abs(tmp-target):
                        ret=tmp
        return ret