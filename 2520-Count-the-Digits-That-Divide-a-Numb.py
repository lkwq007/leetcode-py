class Solution:
    def countDigits(self, num: int) -> int:
        x=num
        ret=0
        while x>0:
            cur=x%10
            if num%cur==0:
                ret+=1
            x=x//10
        return ret