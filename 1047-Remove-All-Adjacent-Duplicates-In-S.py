class Solution:
    def removeDuplicates(self, S: str) -> str:
        ret=[]
        for item in S:
            if ret:
                if ret[-1]==item:
                    ret.pop()
                else:
                    ret.append(item)
            else:
                ret.append(item)
        return "".join(ret)