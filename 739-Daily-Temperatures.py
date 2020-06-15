class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret=[0]*len(T)
        idx=len(T)-2
        total=len(T)
        while idx>=0:
            if T[idx]<T[idx+1]:
                ret[idx]=idx+1
            elif T[idx]==T[idx+1]:
                ret[idx]=ret[idx+1]
            else:
                tmp=ret[idx+1]
                while tmp<total and tmp>0:
                    if T[idx]<T[tmp]:
                        break
                    tmp=ret[tmp]
                ret[idx]=tmp
            idx-=1
        for idx in range(0,total):
            if ret[idx]:
                ret[idx]-=idx
        return ret