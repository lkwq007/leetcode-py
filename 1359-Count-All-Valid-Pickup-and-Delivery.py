class Solution:
    def countOrders(self, n: int) -> int:
        term=10**9+7
        acc=1
        cur=1
        for idx in range(2,n+1):
            cur+=(idx-1)*4+1
            acc*=cur
            acc=acc%term
        return acc