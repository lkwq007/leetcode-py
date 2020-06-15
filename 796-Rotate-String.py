class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if len(A)<1 and len(B)<1:
            return True
        for idx in range(0,len(B)):
            if B[idx]==A[0] and (B[idx:]+B[:idx])==A:
                return True
        return False
