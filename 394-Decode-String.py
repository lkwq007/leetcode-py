class Solution:
    def decodeString(self, s: str) -> str:
        ret=""
        stack=[[1,""]]
        total=len(s)
        idx=0
        while idx<total:
            top=stack[-1]
            if s[idx].isdigit():
                tmp=s[idx]
                idx+=1
                while s[idx]!="[":
                    tmp+=s[idx]
                    idx+=1
                times=int(tmp)
                stack.append([times,""])
            elif s[idx]=="]":
                times,seq=stack.pop()
                tmp=seq*times
                stack[-1][1]+=tmp
            else:
                top[1]+=s[idx]
            idx+=1
        return stack[0][1]