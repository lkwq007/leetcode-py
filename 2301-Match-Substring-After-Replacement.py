class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        # just for fun
        s=s[::-1]
        sub=sub[::-1]
        record={}
        tbl=set(sub)
        for u,v in mappings:
            if v not in record:
                record[v]={}
            if u in tbl:
                record[v][u]=1
        voca=set(s)
        for item in list(voca):
            if item in record:
                for next in record[item].keys():
                    voca.add(next)
        if not (tbl<=voca):
            return False
        prefix=[0]*len(sub)
        for i in range(1,len(sub)):
            j=prefix[i-1]
            while j>0 and sub[j]!=sub[i]:
                j=prefix[j-1]
            if sub[j]==sub[i]:
                j+=1
            prefix[i]=j
        target=len(sub)
        import functools
        import itertools
        @functools.lru_cache(None)
        def probe(pos,prev):
            if pos==len(s):
                return False
            cur=s[pos]
            option=record[cur].keys() if cur in record else []
            lst=set([])
            for item in itertools.chain(cur,option):
                j=prev
                while j>0 and sub[j]!=item:
                    j=prefix[j-1]
                if sub[j]==item:
                    j+=1
                # print(pos,cur,item,j,prev)
                if j==target:
                    return True
                lst.add(j)
            lst=sorted(lst,reverse=True)
            for next in lst:
                if probe(pos+1,next):
                    return True
            return False
        return probe(0,0)
        