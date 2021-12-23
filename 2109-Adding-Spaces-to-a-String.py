class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret=[]
        offset=0
        for i in range(len(s)):
            if offset<len(spaces) and i==spaces[offset]:
                ret.append(" ")
                offset+=1
            ret.append(s[i])
        return "".join(ret)

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret=[]
        left=0
        spaces.append(len(s))
        for idx in spaces:
            # if idx!=left:
            ret.append(s[left:idx])
            left=idx
        return " ".join(ret)
