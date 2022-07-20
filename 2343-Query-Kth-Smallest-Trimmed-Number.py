class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # brute force
        lst=set([])
        for k,t in queries:
            lst.add(t)
        lst=sorted(list(lst))
        record={}
        for key in lst:
            record[key]=[(nums[i][-key:],i) for i in range(len(nums))]
            record[key].sort()
        ret=[]
        for k,t in queries:
            ret.append(record[t][k-1][1])
        return ret