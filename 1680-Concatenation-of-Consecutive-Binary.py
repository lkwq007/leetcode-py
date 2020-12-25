class Solution:
    def concatenatedBinary(self, n: int) -> int:
        term=10**9+7
        acc=0
        def width(x):
            ret=0
            while x>0:
                ret+=1
                x=x>>1
            return ret
        for i in range(n):
            num=i+1
            acc=((acc<<width(num))+num)%term
        return acc

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        term=10**9+7
        acc=0
        cnt=0
        for i in range(n):
            num=i+1
            if num&(num-1)==0:
                cnt+=1
            acc=((acc<<cnt)+num)%term
        return acc