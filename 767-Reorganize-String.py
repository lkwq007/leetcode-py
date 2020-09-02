class Solution:
    def reorganizeString(self, S: str) -> str:
        record={}
        max_val=0
        for item in S:
            record[item]=record.get(item,0)+1
            max_val=max(record[item],max_val)
        if max_val>(len(S)+1)//2:
            return ""
        cnt=0
        total=len(S)
        keys=list(record.keys())
        keys.sort(key=lambda x:-record[x])
        ret=""
        while cnt<total:
            if cnt==total-1:
                ret+=keys[0]
                cnt+=1
                record[keys[0]]-=1
            else:
                ret+=keys[0]+keys[1]
                cnt+=2
                record[keys[0]]-=1
                record[keys[1]]-=1
            keys.sort(key=lambda x:-record[x])
        return ret