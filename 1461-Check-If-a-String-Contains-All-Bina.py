class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s)-k+1<2**k:
            return False
        record=[0]*(2**k)
        mask=1
        for idx in range(1,k):
            mask=mask<<1
            mask|=1
        acc=0
        total=0
        for idx in range(len(s)):
            bit=1 if s[idx]=="1" else 0
            acc=acc<<1
            acc|=bit
            acc&=mask
            if idx>=k-1 and record[acc]==0:
                record[acc]=1
                total+=1
        return total==(2**k)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s)-k+1<2**k:
            return False
        record={}
        mask=(1<<k)-1
        acc=0
        for idx in range(len(s)):
            bit=1 if s[idx]=="1" else 0
            acc=acc<<1
            acc|=bit
            acc&=mask
            if idx>=k-1:
                record[acc]=1
        return len(record)==(2**k)