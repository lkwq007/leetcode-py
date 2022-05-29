class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        record={}        
        for item in s:
            record[item]=record.get(item,0)+1
        cnt={}
        for item in target:
            cnt[item]=cnt.get(item,0)+1
        ret=len(s)
        for k,v in cnt.items():
            ret=min(ret,record.get(k,0)//v)
        return ret