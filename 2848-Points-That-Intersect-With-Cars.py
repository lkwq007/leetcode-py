class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        lst=[0]*102
        for start,end in nums:
            lst[start]+=1
            lst[end+1]-=1
        ret=0
        for i in range(1,len(lst)):
            lst[i]+=lst[i-1]
            if lst[i]>0:
                ret+=1
        return ret
        