class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        template=[0]*(len(nums)+1)
        record=[template[:] for _ in range(101)]
        for i in range(len(nums)):
            record[nums[i]][i]=1
        for i in range(1,101):
            acc=0
            for j in range(len(nums)):
                acc+=record[i][j]
                record[i][j]=acc
        ret=[]
        for l,r in queries:
            last=0
            cnt=0
            diff=200
            for i in range(1,101):
                if record[i][r]-record[i][l-1]>0:
                    if last>0:
                        diff=min(diff,i-last)
                    last=i
            if diff>100:
                ret.append(-1)
            else:
                ret.append(diff)
        return ret