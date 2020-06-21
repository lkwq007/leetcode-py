class Solution:
    def calculate(self, s: str) -> int:
        precedence={"+":0,"-":0,"*":1,"/":1}
        acc=0
        idx=0
        total=len(s)
        num
        while idx<total:
            item=s[idx]
            if item==" ":
                num=0
                continue
            if item.isdigit():
                num=num*10+int(item)
            elif 
