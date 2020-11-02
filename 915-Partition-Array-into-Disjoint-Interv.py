class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left=[A[0]]*(len(A)+1)
        right=[A[-1]]*(len(A)+1)
        for i in range(len(A)):
            left[i]=max(A[i],left[i-1])
            idx=len(A)-i-1
            right[idx]=min(A[idx],right[idx+1])
        for i in range(len(A)-1):
            if left[i]<=right[i+1]:
                return i+1