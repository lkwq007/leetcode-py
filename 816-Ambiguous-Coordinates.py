class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        S=S[1:-1]
        ret=[]
        def probe(s):
            lst=[]
            if str(int(s))==s:
                lst.append(s)
            for i in range(1,len(s)):
                left=s[:i]
                right=s[i:]
                tmp=left+"."+right
                if str(int(left))==left and right[-1]!="0":
                    lst.append(tmp)
            return lst
        for i in range(1,len(S)):
            left=probe(S[:i])
            right=probe(S[i:])
            for l in left:
                for r in right:
                    ret.append(f"({l}, {r})")
        return ret