class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        idx=len(S)-1
        cnt=0
        acc=""
        ret=[]
        while idx>=0:
            if S[idx]=="-":
                idx-=1
                continue
            if len(acc)==K:
                ret.append(acc)
                acc=S[idx].upper()
            else:
                acc=S[idx].upper()+acc
            idx-=1
        if acc:
            ret.append(acc)
        return "-".join(reversed(ret))