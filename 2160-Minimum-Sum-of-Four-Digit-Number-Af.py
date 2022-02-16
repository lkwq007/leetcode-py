class Solution:
    def minimumSum(self, num: int) -> int:
        lst=list(map(int,str(num)))
        lst.sort()
        return (lst[0]+lst[1])*10+lst[2]+lst[3]
class Solution:
    def minimumSum(self, num: int) -> int:
        lst=list(map(int,str(num)))
        lst.sort()
        ret=num
        for i in range(4):
            for j in range(i+1,4):
                acc=0
                for k in range(4):
                    if k!=i and k!=j:
                        acc*=10
                        acc+=lst[k]
                ret=min(lst[i]*10+lst[j]+acc,ret)
        return ret