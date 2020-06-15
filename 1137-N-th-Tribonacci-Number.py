class Solution:
    def tribonacci(self, n: int) -> int:
        item=[0,1,1]
        if n<3:
            return item[n]
        n-=2
        idx=0
        while n>0:
            n-=1
            current=sum(item)
            item[idx]=current
            idx=(idx+1)%3
        return current