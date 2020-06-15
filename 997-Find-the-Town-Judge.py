class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        score=[0]*(N+1)
        Nminus1=N-1
        for truster,trustee in trust:
            score[trustee]+=1
            score[truster]-=1
        for idx in range(1,N+1):
            if score[idx]==Nminus1:
                return idx
        return -1
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1 and len(trust)==0:
            return 1
        template=[0,0]
        counter=[template[:] for i in range(0,N+1)]
        lst=[]
        Nminus1=N-1
        for item in trust:
            truster=item[0]
            trustee=item[1]
            counter[truster][0]+=1
            counter[trustee][1]+=1
            if counter[trustee][1]==Nminus1:
                lst.append(trustee)
        for item in lst:
            if counter[item][0]==0 and counter[item][1]==Nminus1:
                return item
        return -1