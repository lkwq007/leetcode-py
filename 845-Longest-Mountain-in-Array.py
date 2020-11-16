class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        ret=0
        leftmost=-1
        flag=False
        for i in range(len(A)-1):
            if A[i+1]>A[i]:
                if leftmost==-1 or flag:
                    leftmost=i
                flag=False
            elif A[i+1]<A[i]:
                flag=True
                if leftmost!=-1:
                    ret=max(ret,i+1-leftmost+1)
            else:
                leftmost=-1
        return ret