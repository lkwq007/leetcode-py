class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        def judge(x):
            ret=0
            for item in nums:
                if item%x!=0:
                    ret+=1
                ret+=item//x
            return ret<=threshold
        while left<right:
            middle=left+(right-left)//2
            if judge(middle):
                right=middle
            else:
                left=middle+1
        return left