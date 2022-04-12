class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        stack=[]
        for i in range(len(s)):
            if locked[i]=="1":
                if s[i]=="(":
                    stack.append((s[i],locked[i]))
                else:
                    if len(stack)==0 or stack[-1]==(")","1"):
                        return False
                    elif stack[-1]==("(","1"):
                        stack.pop()
            else:
                if len(stack)==0:
                    stack.append(("(","1"))
                else:
                    stack.append(("*","0"))
        acc=0
        for i in range(len(stack)-1,-1,-1):
            if stack[i][1]=="0":
                acc+=1
            else:
                if acc==0:
                    return False
                acc-=1
        return True