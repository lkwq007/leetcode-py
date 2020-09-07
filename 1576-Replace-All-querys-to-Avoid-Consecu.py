class Solution:
    def modifyString(self, s: str) -> str:
        lst=list(s)
        template=[chr(ord("a")+i) for i in range(26)]
        for i in range(len(lst)):
            if lst[i]!="?":
                continue
            left="" if i==0 else lst[i-1]
            right="" if i==len(lst)-1 else lst[i+1]
            for c in template:
                if c!=left and c!=right:
                    lst[i]=c
                    break
        return "".join(lst)
