class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total=sum(nums)
        ret=0
        val=total+1
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            total-=nums[i]
            if i!=len(nums)-1:
                if abs(acc//(i+1)-total//(len(nums)-i-1))<val:
                    ret=i
                    val=abs(acc//(i+1)-total//(len(nums)-i-1))
            else:
                if acc//len(nums)<val:
                    ret=i
        return ret
