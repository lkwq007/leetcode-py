class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        disjoint=[-1]*len(A)
        total=len(A)
        def find(x):
            ret=x
            while disjoint[ret]>-1:
                ret=disjoint[ret]
            while disjoint[x]>-1:
                tmp=disjoint[x]
                disjoint[x]=ret
                x=tmp
            return ret
        def cmp(a,b):
            cnt=0
            for x,y in zip(a,b):
                if x!=y:
                    cnt+=1
            return cnt<=2
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if cmp(A[i],A[j]):
                    idx1=find(i)
                    idx2=find(j)
                    if idx1!=idx2:
                        disjoint[idx2]=idx1
                        total-=1
        return total
            