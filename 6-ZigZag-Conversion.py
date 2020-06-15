class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        item=numRows*2-2
        total=len(s)
        ret=""
        for row in range(numRows):
            if row==0 or row==numRows-1:
                base=row
                idx=base
                while idx<total:
                    ret+=s[idx]
                    idx+=item
            else:
                base1=row
                base2=item-row
                while base1<total and base2<total:
                    ret=ret+s[base1]+s[base2]
                    base1+=item
                    base2+=item
                if base1<total:
                    ret+=s[base1]
        return ret
                