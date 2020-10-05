class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        # non-negative integers, we can always jump to last index
        start=0
        target=0
        step=0
        total=len(nums)
        while target<total-1:
            step+=1
            max_end=target+1
            for idx in range(start,target+1):
                max_end=max(max_end,nums[idx]+idx)
            if max_end>=total-1:
                return step
            target=max_end
            start=target+1
        return step