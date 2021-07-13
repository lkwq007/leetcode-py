class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ret=1
        lst=[A[i]-i for i in range(len(A))]
        acc=lst[-1]
        for i in range(len(A)-2,-1,-1):
            ret=max(A[i]+acc+i,ret)
            acc=max(acc,lst[i])
        return ret


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ret=1
        acc=A[-1]-len(A)+1
        for i in range(len(A)-2,-1,-1):
            ret=max(A[i]+acc+i,ret)
            acc=max(acc,A[i]-i)
        return ret

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ret=0
        # brute force, TLE
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                ret=max(A[j]+A[i]+i-j,ret)
        return ret