class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ret=[]
        idx=list(range(len(indices)))
        idx.sort(key=lambda x:indices[x])
        last=0
        for i in idx:
            cur,src,tgt=indices[i],sources[i],targets[i]
            if s[cur:cur+len(src)]==src:
                ret.append(s[last:cur])
                ret.append(tgt)
                last=cur+len(src)
        ret.append(s[last:len(s)])
        return "".join(ret)