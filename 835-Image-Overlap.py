class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # brute force
        bits=[1<<i for i in range(30)]
        def count(lst):
            ret=0
            for item in lst:
                while item>0:
                    if item&1:
                        ret+=1
                    item=item>>1
            return ret
        A_=A
        B_=B
        def convert(lst):
            ret=0
            for i in range(len(lst)):
                if lst[i]:
                    ret+=bits[i]
            return ret
        A=[convert(lst) for lst in A]
        B=[convert(lst) for lst in B]
        ret=0
        for i in range(len(A)):
            for j in range(len(A)):
                tmp=[(a&(b>>j),(a>>j)&b,c&(d>>j),(c>>j)&d) for a,b,c,d in zip(A[i:],B[:len(A)-i],A[:len(A)-i],B[i:])]
                for item in zip(*tmp):
                    ret=max(ret,count(item))
        return ret