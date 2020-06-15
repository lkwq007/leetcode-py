class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        len_p=len(p)
        len_s=len(s)
        record_p={}
        record_s={}
        template=[chr(x) for x in range(ord("a"),ord("z")+1)]
        for item in template:
            record_p[item]=0
            record_s[item]=0
        for item in p:
            record_p[item]+=1
        idx=0
        while idx<len_p:
            record_s[s[idx]]+=1
            idx+=1
        idx=0
        total=len_s-len_p
        ret=[]
        while idx<=total:
            if record_p==record_s:
                ret.append(idx)
            record_s[s[idx]]-=1
            if idx+len_p<len_s:
                record_s[s[idx+len_p]]+=1
            idx+=1
        return ret