class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        last=K%10
        if last in [0,2,4,5,6,8]:
            return -1
        def fill(x):
            if x==0:
                s=""
                left=int("1"*lenK)
            else:
                s=str(x)
                left=int(s+"1"*(lenK-len(s)))
            if left<K:
                left=left*10+1
            return left,len(str(left))-len(s)
        lenK=len(str(K))
        left,ret=fill(0)
        record={}
        record[left]=1
        while True:
            r=left%K
            if r==0:
                return ret
            left,acc=fill(r)
            ret+=acc
            if left in record:
                return -1
        return -1