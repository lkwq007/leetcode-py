class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # min max
        mask=1
        mapping=[0]*len(cookies)
        for i in range(len(cookies)):
            mapping[i]=mask
            mask=mask<<1
        if len(cookies)<=k:
            return max(cookies)
        total=sum(cookies)
        import functools
        @functools.lru_cache(None)
        def probe(state,pos):
            if pos==len(cookies):
                return max(state)
            lst=list(state)
            ret=total
            for i in range(len(state)):
                lst[i]+=cookies[pos]
                ret=min(ret,probe(tuple(lst),pos+1))
                lst[i]-=cookies[pos]
            return ret
        return probe((0,)*k,0)