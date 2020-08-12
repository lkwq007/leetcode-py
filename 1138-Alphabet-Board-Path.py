class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        mapping={"z":(5,0)}
        base=ord("a")
        for y in range(5):
            for x in range(5):
                item=chr(base+x+y*5)
                mapping[item]=(y,x)
        ret=[]
        y=0
        x=0
        for item in target:
            y1,x1=mapping[item]
            if y1!=y and y==5:
                y-=1
                ret.append("U")
            elif y1==5 and x>0:
                ret.append("L"*x)
                x=0
            horizontal="L"*(x-x1) if x>x1 else "R"*(x1-x)
            vertical="U"*(y-y1) if y>y1 else "D"*(y1-y)
            ret.append(horizontal)
            ret.append(vertical)
            ret.append("!")
            y=y1
            x=x1
        return "".join(ret)