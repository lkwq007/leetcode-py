class Solution:
    def minDeletions(self, s: str) -> int:
        record={}
        meta={}
        for item in s:
            record[item]=record.get(item,0)+1
        for k,v in record.items():
            meta[v]=meta.get(v,0)+1
        ret=0
        keys=list(meta.keys())
        keys.sort(key=lambda x:-x)
        for key in keys:
            if meta[key]>1:
                acc=meta[key]-1
                ret+=acc
                idx=key-1
                while idx>0 and acc>0:
                    if idx not in meta:
                        acc-=1
                    else:
                        meta[idx]+=acc
                        break
                    ret+=acc
                    idx-=1
        return ret
