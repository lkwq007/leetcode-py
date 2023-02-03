class Solution:
    def captureForts(self, forts: List[int]) -> int:
        lst=[-1]*3
        ret=0
        for i in range(len(forts)):
            cur=forts[i]
            if cur!=0 and lst[cur]<lst[-cur]:
                ret=max(ret,i-lst[-cur]-1)
            lst[cur]=i
        return ret