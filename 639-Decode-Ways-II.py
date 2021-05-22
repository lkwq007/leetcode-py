import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)<1 or s[0]=="0":
            return 0
        term=10**9+7
        @functools.lru_cache(maxsize=None)
        def probe(idx,concat=0):
            # hard start from idx, num of decode ways
            if idx==len(s):
                return 1 if concat==0 else 0
            if concat==0:
                if s[idx]=="0":
                    return 0
                elif s[idx]=="*":
                    return (9*probe(idx+1,0)+probe(idx+1,1)+probe(idx+1,2))%term
                elif int(s[idx])>2:
                    return probe(idx+1,0)
                else:
                    return (probe(idx+1,0)+probe(idx+1,int(s[idx])))%term
            elif concat==2:
                if s[idx]=="*":
                    return (6*probe(idx+1,0))%term
                elif 0<=int(s[idx])<=6:
                    return probe(idx+1,0)
                else:
                    return 0
            else:
                if s[idx]=="*":
                    return (9*probe(idx+1,0))%term
                return probe(idx+1,0)
        return probe(0,0)