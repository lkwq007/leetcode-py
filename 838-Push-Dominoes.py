class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left=False
        right=False
        free=0
        ret=[]
        for item in dominoes:
            if item=="L":
                if right:
                    l=free//2
                    r=free//2
                    m=free%2
                    ret.append("R"*r)
                    ret.append("."*m)
                    ret.append("L"*l)
                else:
                    ret.append("L"*free)
                right=False
                free=0
                ret.append(item)
            elif item=="R":
                ret.append(("R" if right else ".")*free)
                free=0
                ret.append(item)
                right=True
            else:
                free+=1
        ret.append(("R" if right else ".")*free)
        return "".join(ret)