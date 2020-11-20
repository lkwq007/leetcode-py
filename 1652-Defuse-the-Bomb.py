class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ret=[0]*len(code)
        if k==0:
            return ret
        total=len(code)
        acc=0
        if k>0:
            for i in range(k):
                acc+=code[i]
            for i in range(len(code)):
                acc=acc-code[i]+code[(i+k)%total]
                ret[i]=acc
        else:
            for i in range(-k):
                acc+=code[-1-i]
            for i in range(len(code)):
                ret[i]=acc
                acc=acc+code[i]-code[(i+k+total)%total]
        return ret
