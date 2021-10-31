class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        total=len(s)
        left=[-1]*total
        right=[-1]*total
        prefix=[0]*(total+1)
        acc=0
        last=-1
        for i in range(total):
            if s[i]=="*":
                acc+=1
            else:
                last=i
            left[i]=last
            prefix[i]=acc
        last=-1
        for i in range(total-1,-1,-1):
            if s[i]=="|":
                last=i
            right[i]=last
        ret=[]
        for l,r in queries:
            l_idx=right[l]
            r_idx=left[r]
            if l_idx<r_idx and l_idx!=-1 and r_idx!=-1:
                ret.append(prefix[r_idx]-prefix[l_idx])
            else:
                ret.append(0)
        return ret