class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        total=len(nums)+maxOperations
        max_val=max(nums)
        left=1
        right=max_val
        while left<right:
            middle=left+(right-left)//2
            acc=0
            for item in nums:
                if item%middle==0:
                    val=item//middle
                else:
                    val=(item//middle)+1
                acc+=val
            if acc>total:
                left=middle+1
            else:
                right=middle
        return left