class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # num of good pairs?
        acc=0
        # nums[j]-j == nums[i]-i
        record={}
        for i in range(len(nums)):
            cur=nums[i]-i
            acc+=record.get(cur,0)
            record[cur]=record.get(cur,0)+1
        return len(nums)*(len(nums)-1)//2-acc