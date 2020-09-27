class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        acc=0
        for item in A:
            if item&1==0:
                acc+=item
        ret=[0]*len(queries)
        for i in range(len(queries)):
            val,index=queries[i]
            tmp=val+A[index]
            if tmp&1:
                if A[index]&1==0:
                    acc-=A[index]
            else:
                if A[index]&1:
                    acc+=tmp
                else:
                    acc+=val
            A[index]=tmp
            ret[i]=acc
        return ret
