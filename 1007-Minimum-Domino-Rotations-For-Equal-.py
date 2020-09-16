class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ret=len(A)
        a=A[0]
        b=B[0]
        top=1 if a!=b else 0
        bottom=0
        flag=False
        for i in range(1,len(A)):
            if A[i]==a and B[i]==a:
                continue
            elif A[i]==a:
                top+=1
            elif B[i]==a:
                bottom+=1
            else:
                flag=True
                break
        if a==b or not flag:
            return -1 if flag else min(top,bottom)
        bottom=1
        top=0
        flag=False
        for i in range(1,len(A)):
            if A[i]==b and B[i]==b:
                continue
            elif A[i]==b:
                top+=1
            elif B[i]==b:
                bottom+=1
            else:
                flag=True
                break
        return -1 if flag else min(top,bottom)