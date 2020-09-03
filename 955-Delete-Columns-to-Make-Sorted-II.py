class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A)<2:
            return 0
        ret=0
        total=len(A[0])
        lst=[i for i in range(len(A))]
        for i in range(total):
            target=[]
            for j in lst:
                if j!=len(A)-1:
                    if A[j][i]==A[j+1][i]:
                        target.append(j)
                    elif A[j][i]>A[j+1][i]:
                        ret+=1
                        target=lst
                        break
            lst=target
        return ret
