class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        ones=0
        for item in S:
            if item=="1":
                ones+=1
        total=len(S)
        zeros=total-ones
        ret=zeros
        acc0=0
        acc1=0
        for i in range(len(S)):
            if S[i]=="1":
                acc1+=1
            else:
                acc0+=1
            ret=min(ret,acc1+zeros-acc0)
        return ret