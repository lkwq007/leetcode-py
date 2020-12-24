class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        acc=0
        ret=[False]*len(A)
        for i,num in enumerate(A,0):
            acc=(acc*2+num)%5
            if acc==0:
                ret[i]=True
        return ret
