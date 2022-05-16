class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # 1 <= boxes.length <= 100
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
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(start,end):
            if start==end:
                return lst[start][1]*lst[start][1]
            if start>end:
                return 0
            cur,acc=lst[start]
            idx=start+1
            ret=0
            other=0
            while idx<=end:
                ret=max(ret,acc*acc+other+probe(idx,end))
                if cur==lst[idx][0]:
                    acc+=
                    ret=max(ret,)


        return probe(0,len(lst)-1)
                
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