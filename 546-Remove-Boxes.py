class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # TLE
        cnt=1
        last=-1
        lst=[]
        for item in boxes:
            if item==last:
                cnt+=1
            elif last!=-1:
                lst.append((last,cnt))
                cnt=1
            last=item
        lst.append((last,cnt))
        ret=0
        dp=[[0]*100 for _ in range(100)]
        for i in range(1,len(lst)):
            for j in range(len(lst)):
                for k in range(j,min(j+i,len(lst))):
                    if j==k:
                        dp[j][k]=lst[j][1]*lst[j][1]
                    


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # TLE
        cnt=1
        last=-1
        lst=[]
        for item in boxes:
            if item==last:
                cnt+=1
            elif last!=-1:
                lst.append((last,cnt))
                cnt=1
            last=item
        lst.append((last,cnt))
        # print(lst)
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(state):
            ret=0
            for i in range(len(state)):
                val=state[i][1]*state[i][1]
                if i==0 or i==len(state)-1:
                    ret=max(ret,val+probe(state[:i]+state[i+1:]))
                else:
                    if state[i-1][0]==state[i+1][0]:
                        ret=max(ret,val+probe(state[:i-1]+((state[i+1][0],state[i+1][1]+state[i-1][1]),)+state[i+2:]))
                    else:
                        ret=max(ret,val+probe(state[:i]+state[i+1:]))
            return ret
        return probe(tuple(lst))