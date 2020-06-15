class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        idx=0
        total=len(s)
        while idx<total:
            item=s[idx]
            if item.isdigit():
                tmp=""
                while s[idx].isdigit():
                    tmp+=s[idx]
                    idx+=1
                num=int(tmp)
            elif item=="(":
                pass
            elif item==")":
                pass
            elif item=="+":
                
            elif item=="-":
                pass
            else:
                idx+=1