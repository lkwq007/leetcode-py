class Solution:
    def isUgly(self, num: int) -> bool:
        if num<1:
            return False
        if num==1:
            return True
        tmp=num
        factor=[2,3,5]
        idx=0
        while num>1:
            if num%factor[idx]==0:
                num=num//factor[idx]
            else:
                idx+=1
            if idx>2:
                return False
        return True