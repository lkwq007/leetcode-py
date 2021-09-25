class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)&1:
            return []
        record={}
        for item in changed:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:-x)
        ret=[]
        for k in keys:
            cnt=record[k]
            if cnt==0:
                continue
            if k==0:
                if cnt&1:
                    return []
                else:
                    ret+=[0]*(cnt//2)
                break              
            if k&1 or record.get(k//2,0)<cnt:
                return []
            ret+=[k//2]*cnt
            record[k//2]-=cnt
        return ret