class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N<=2:
            return True
        lst=[0]*10
        x=N
        while x>0:
            lst[x%10]+=1
            x=x//10
        acc=2
        for i in range(31):
            acc=acc<<1
            cur_lst=[0]*10
            tmp=acc
            while tmp>0:
                cur_lst[tmp%10]+=1
                tmp=tmp//10
            if cur_lst==lst:
                return True
        return False