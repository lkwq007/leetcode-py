class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ret=[0]*len(queries)
        lst=[(queries[i],i) for i in range(len(queries))]
        lst.sort()
        acc=0
        pos=0
        for i in range(len(lst)):
            cur,idx=lst[i]
            while pos<len(nums) and acc+nums[pos]<=cur:
                acc+=nums[pos]
                pos+=1
            ret[idx]=pos
        return ret