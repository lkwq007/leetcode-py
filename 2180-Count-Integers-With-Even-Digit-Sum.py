class Solution:
    def countEven(self, num: int) -> int:
        ret=0
        while num>0:
            acc=0
            x=num
            while x>0:
                acc+=(x%10)
                x=x//10
            if acc%2==0:
                ret+=1
            num-=1
        return ret