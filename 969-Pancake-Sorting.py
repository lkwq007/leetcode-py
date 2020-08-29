class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # a straightforward manner
        indice=[0]*len(A)
        for idx in range(len(A)):
            indice[A[idx]-1]=idx
        ret=[]
        for i in range(len(A)-1,0,-1):
            idx=indice[i]
            if idx==i:
                continue
            if idx!=0:
                ret.append(idx+1)
            ret.append(i+1)
            indice[i]=i
            for j in range(i):
                if indice[j]>idx:
                    indice[j]=i-indice[j]
                else:
                    indice[j]=i-1-(idx-1-indice[j])
        return ret