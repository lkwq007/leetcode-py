class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lst=list(s)
        stack=[]
        for i in range(len(lst)):
            if lst[i]=="(":
                stack.append(i)
            elif lst[i]==")":
                if stack:
                    stack.pop()
                else:
                    lst[i]=""
        for idx in stack:
            lst[idx]=""
        return "".join(lst)                    