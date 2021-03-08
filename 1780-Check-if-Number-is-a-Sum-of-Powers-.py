class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        cur=1
        while cur<n:
            cur*=3
        while cur>=1:
            if n>=cur:
                n-=cur
            cur=cur//3
        return n<1

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        cur=1
        while cur<n:
            cur*=3
        while cur>1:
            if n>=cur:
                n-=cur
            cur=cur//3
        return n<=1