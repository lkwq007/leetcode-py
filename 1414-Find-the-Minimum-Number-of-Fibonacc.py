class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        lst=[1,1]
        a=1
        b=1
        while b<=k:
            b,a=a+b,b
        ret=0
        while k!=0:
            if k-b>=0:
                k-=b
                ret+=1
            else:
                b,a=a,b-a
        return ret
