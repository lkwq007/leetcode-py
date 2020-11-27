class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        for item in nums:
            total+=item
        if total%2==1:
            return False
        half=total//2
        for item in nums:
            if item>half:
                return False
            elif item==half:
                return True
        nums.sort()
        self.ret=False
        import functools
        @functools.lru_cache(maxsize=None)
        def check(i,acc):
            if i==len(nums) or self.ret:
                return
            if nums[i]+acc==half:
                self.ret=True
                return
            check(i+1,acc)
            check(i+1,acc+nums[i])
        check(0,0)
        return self.ret