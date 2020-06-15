class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt=0
        while num>0:
            cnt+=1
            if num%2:
                num-=1
            else:
                num=num//2
        return cnt