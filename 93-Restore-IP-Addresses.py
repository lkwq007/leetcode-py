class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<4:
            return []
        def probe(rest,num):
            if not rest:
                return []
            if num==1:
                if 1<=len(rest)<=3 and 0<=int(rest)<=255:
                    if len(rest)>1 and rest[0]=="0":
                        return []
                    return [rest]
                return []
            ret=[]
            if rest[0]=="0":
                cur=rest[0]
                lst=probe(rest[1:],num-1)
                for item in lst:
                    ret.append(cur+"."+item)
            else:
                for i in range(3):
                    cur=rest[:(i+1)]
                    if 0<=int(cur)<=255:
                        lst=probe(rest[(i+1):],num-1)
                        for item in lst:
                            ret.append(cur+"."+item)
            return ret
        return probe(s,4)