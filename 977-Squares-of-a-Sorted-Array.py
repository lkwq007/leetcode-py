class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ret=[0]*len(A)
        neg=0
        pos=len(A)-1
        for idx in range(len(A)-1,-1,-1):
            if abs(A[neg])>abs(A[pos]):
                ret[idx]=A[neg]*A[neg]
                neg+=1
            else:
                ret[idx]=A[pos]*A[pos]
                pos-=1
        return ret

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A)<1:
            return A
        ret=[]
        left=0
        right=len(A)-1
        while left<right:
            middle=left+(right-left)//2
            if A[middle]==0:
                left=middle
                break
            elif A[middle]>0:
                right=middle
            else:
                left=middle+1
        if A[left]==0:
            neg=left-1
            pos=left+1
            ret.append(0)
        elif A[left]>0:
            pos=left
            neg=left-1
        else:
            neg=left
            pos=left+1
        while neg>=0 and pos<len(A):
            if A[neg]*A[neg]<A[pos]*A[pos]:
                ret.append(A[neg]*A[neg])
                neg-=1
            else:
                ret.append(A[pos]*A[pos])
                pos+=1
        while neg>=0:
            ret.append(A[neg]*A[neg])
            neg-=1
        while pos<len(A):
            ret.append(A[pos]*A[pos])
            pos+=1
        return ret
        