class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<11:
            return []
        mapping={
            "A":0,"C":1,"G":2,"T":3
        }
        record={}
        acc=0
        mask=0x0FFFFF
        ret=[]
        for idx in range(10):
            item=mapping[s[idx]]
            acc=acc<<2
            acc|=item
        record[acc]=1
        for idx in range(10,len(s)):
            item=mapping[s[idx]]
            acc=acc<<2
            acc|=item
            acc&=mask
            cnt=record.get(acc,0)
            if cnt==1:
                ret.append(s[idx-9:idx+1])
            record[acc]=cnt+1
        return ret                
