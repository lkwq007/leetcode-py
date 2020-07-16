class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        base_a=ord("a")
        base_0=ord("0")
        def to_hex(x):
            ret=""
            while x>0:
                cur=x%16
                x=x//16
                if cur>9:
                    item=chr(base_a+cur-10)
                else:
                    item=chr(base_0+cur)
                ret=item+ret
            return ret
        if num<0:
            mask=0xffffffff
            num=-num
            num=((~num)+1)&mask
        return to_hex(num)
