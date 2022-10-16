class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        cur=0
        lst=[]
        while n>0:
            if n&1:
                lst.append(cur)
            n=n>>1
            cur+=1
        prefix=[0]*(len(lst)+1)
        for i in range(len(lst)):
            prefix[i]=lst[i]+prefix[i-1]
        ret=[]
        term=10**9+7
        for l,r in queries:
            total=prefix[r]-prefix[l-1]
            ret.append(pow(2,total,term))
        return ret