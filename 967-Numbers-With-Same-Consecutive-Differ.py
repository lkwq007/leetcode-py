import functools
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N==1:
            return [i for i in range(10)]
        @functools.lru_cache(maxsize=None)
        def probe(pos,last):
            tup=(-K,K) if K>0 else (0,)
            if pos==N-1:
                return [str(last+item) for item in tup if 0<=last+item<10]
            ret=[]
            for item in tup:
                cur=last+item
                cur_str=str(cur)
                if 0<=cur<10:
                    lst=probe(pos+1,cur)
                else:
                    lst=[]
                for seq in lst:
                    ret.append(cur_str+seq)
            return ret
        ret=[]
        for i in range(1,10):
            cur=str(i)
            for item in probe(1,i):
                ret.append(int(cur+item))
        return ret
