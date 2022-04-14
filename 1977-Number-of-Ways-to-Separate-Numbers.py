class Solution:
    def numberOfCombinations(self, num: str) -> int:
        # TLE
        term=10**9+7
        if num[0]=="0":
            return 0
        record={}
        def probe(pos,last):
            if (pos,last) in record:
                return record[(pos,last)]
            # print(pos,last)
            len_last=pos-last
            if len(num)-pos<len_last:
                record[(pos,last)]=0
                return 0
            idx=pos+len(last)
            cur=num[pos:idx]
            last_val=num[last:pos] if last>=0 else "0"
            if cur<last_val:
                idx+=1
            ret=1 if idx<=len(num) else 0
            for i in range(len(num),idx-1,-1):
                if i<len(num) and num[i]=="0":
                    continue
                tmp=probe(i,pos)
                for j in range(pos+1,i):
                    if num[j]!=0:
                        record[(i,j)]=tmp
                ret+=tmp
                ret%=term
            record[(pos,last)]=ret
            return ret
        return probe(0,-1)

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        # TLE
        term=10**9+7
        if num[0]=="0":
            return 0
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(pos,last):
            # print(pos,last)
            if len(num)-pos<len(last):
                return 0
            idx=pos+len(last)
            cur=num[pos:idx]
            if cur<last:
                idx+=1
            ret=1 if idx<=len(num) else 0
            for i in range(idx,len(num)+1):
                if i<len(num) and num[i]=="0":
                    continue
                ret+=probe(i,num[pos:i])
                ret%=term
            return ret
        return probe(0,"0")