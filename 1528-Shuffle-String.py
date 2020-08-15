class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ret=list(s)
        for i in range(len(indices)):
            ret[indices[i]]=s[i]
        return "".join(ret)

#  cyclic sort
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ret=list(s)
        for i in range(len(indices)):
            while indices[i]!=i:
                tmp=indices[i]
                ret[i],ret[indices[i]]=ret[indices[i]],ret[i]
                indices[i],indices[tmp]=indices[tmp],indices[i]
        return "".join(ret)