class Solution:
    def numSteps(self, s: str) -> int:
        acc=0
        carry=0
        for idx in range(len(s)-1,0,-1):
            cur=1 if s[idx]=="1" else 0
            if cur+carry==0:
                acc+=1
                carry=0
            elif cur+carry==1:
                acc+=2
                carry=1
            else:
                acc+=1
                carry=1
        if carry:
            acc+=1
        return acc
                