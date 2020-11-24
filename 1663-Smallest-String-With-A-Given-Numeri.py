class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        rest=k-n
        z=rest//25
        another=rest%25
        base=ord("a")
        if another>0:
            ret="a"*(n-z-1)+chr(another+base)+"z"*z
        else:
            ret="a"*(n-z)+"z"*z
        return ret

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        total=k
        lst=[]
        for i in range(n):
            right=26*(n-i-1)
            if total-1<=right:
                lst.append(1)
                total-=1
            else:
                cur=total-right
                lst.append(cur)
                total-=cur
        return "".join([chr(ord("a")+item-1) for item in lst])

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        total=k
        lst=[""]*n
        base=ord("a")-1
        for i in range(n):
            right=26*(n-i-1)
            if total-1<=right:
                cur=1
            else:
                cur=total-right
            lst[i]=chr(base+cur)
            total-=cur
        return "".join(lst)