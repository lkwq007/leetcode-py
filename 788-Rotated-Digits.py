class Solution:
    def rotatedDigits(self, N: int) -> int:
        set_invalid=set([3,4,7])
        set_diff=set([2,5,6,9])
        ret=0
        for i in range(N):
            num=i+1
            invalid=0
            diff=0
            while num>0:
                cur=num%10
                if cur in set_diff:
                    diff+=1
                elif cur in set_invalid:
                    invalid+=1
                num=num//10
            if invalid==0 and diff>0:
                ret+=1
        return ret