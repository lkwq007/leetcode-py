class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        if len1>len2:
            return False
        record1={}
        record2={}
        base=ord("a")
        for i in range(0,26):
            item=chr(base+i)
            record1[item]=0
            record2[item]=0
        for idx in range(0,len1):
            record1[s1[idx]]+=1
            record2[s2[idx]]+=1
        total=len2-len1+1
        for idx in range(0,total):
            if record1==record2:
                return True
            record2[s2[idx]]-=1
            if idx+len1<len2:
                record2[s2[idx+len1]]+=1
        return False