class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        max_idx=0
        for idx in range(0,len(nums)):
            if nums[idx]>nums[max_idx]:
                max_idx=idx
        ret=[-1]*len(nums)
        stack=[nums[max_idx]]
        total=len(nums)
        idx=(max_idx-1+total)%total
        while idx!=max_idx:
            item=nums[idx]
            while stack:
                if stack[-1]>item:
                    break
                else:
                    stack.pop()
            if stack:
                ret[idx]=stack[-1]
            stack.append(item)
            idx=(idx-1+total)%total
        return ret