class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        if len(nums)<2:
            return min(abs(goal),abs(nums[0]-goal))
        def probe(start,end,record):
            if start==end:
                return {0:1}
            lst=probe(start+1,end)
            keys=list(lst.keys())
            for key in keys:
                lst[key+nums[start]]=1
            return lst
        total=len(nums)
        lst1=probe(0,total//2)
        lst2=probe(total//2,total)
        lst2=list(sorted(lst2.keys()))
        ret=abs(goal)
        for item in lst1.keys():
            left=0
            right=len(lst2)-1
            target=goal-item
            while left<right:
