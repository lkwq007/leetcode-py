class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<3:
            return False
        x=num
        acc=1
        factor=2
        while factor*factor<=x:
            if num%factor==0:
                acc+=factor
                if factor*factor!=num:
                    acc+=num//factor
            factor+=1
        return acc==num