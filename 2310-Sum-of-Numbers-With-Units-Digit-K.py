class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0:
            return 0
        if k==0:
            if num%10==0:
                return 1
            else:
                return -1
        total=(num+k-1)//k
        def check(x):
            cur=x*k
            rest=num-cur
            if rest<0 or rest%10!=0:
                return False
            return True
        for i in range(1,total+1):
            if check(i):
                return i
        return -1