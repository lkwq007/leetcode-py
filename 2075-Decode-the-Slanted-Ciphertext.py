class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # the basic idea is to get correct pos
        ret=[]
        col=len(encodedText)//rows
        for x0 in range(col):
            y=0
            x=x0
            while y<rows and x<col:
                ret.append(encodedText[y*col+x])
                y+=1
                x+=1
        while ret and ret[-1]==" ":
            ret.pop()
        return "".join(ret)