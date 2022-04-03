class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        prefix=[0]*(len(floor)+1)
        for i in range(len(floor)):
            prefix[i]=prefix[i-1]+int(floor[i])
        total=prefix[-2]
        import functools
        @functools.lru_cache(None)
        def probe(pos,k):
            if pos>=len(floor) or k==0:
                return 0
            ret=0
            while pos<len(floor) and floor[pos]=="0":
                pos+=1
            if len(floor)-pos<carpetLen:
                ret=prefix[-2]-prefix[pos-1]
            else:
                ret=max(prefix[pos+carpetLen-1]-prefix[pos-1]+probe(pos+carpetLen,k-1),probe(pos+1,k))
            # print(pos,k,ret)
            return ret
        return total-probe(0,numCarpets)
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        # TLE
        prefix=[0]*(len(floor)+1)
        for i in range(len(floor)):
            prefix[i]=prefix[i-1]+int(floor[i])
        total=prefix[-2]
        import functools
        @functools.lru_cache(None)
        def probe(pos,k):
            if pos>=len(floor) or k==0:
                return 0
            ret=0
            if len(floor)-pos<carpetLen:
                ret=prefix[-2]-prefix[pos-1]
            else:
                for i in range(pos,len(floor)-carpetLen+1):
                    ret=max(prefix[i+carpetLen-1]-prefix[i-1]+probe(i+carpetLen,k-1),ret)
            return ret
        return total-probe(0,numCarpets)