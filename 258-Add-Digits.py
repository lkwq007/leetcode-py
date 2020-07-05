class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            s=str(num)
            num=sum(map(int,s))
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        if num%9==0:
            return 9
        return num%9