class Solution:
    def sortString(self, s: str) -> str:
        ret=[]
        record={}
        for item in s:
            record[item]=record.get(item,0)+1
        total=0
        keys=list(sorted(record.keys()))
        idx=0
        offset=1
        while total<len(s):
            key=keys[idx]
            if record[key]>0:
                ret.append(key)
                record[key]-=1
                total+=1
            idx+=offset
            if idx==len(keys) or idx<0:
                idx-=offset
                offset=-offset
        return "".join(ret)