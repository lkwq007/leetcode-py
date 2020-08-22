class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[""]
        ret=0
        for item in s:
            if item==")":
                if stack[-1]==")":
                    stack.pop()
                elif stack[-1]=="(":
                    stack[-1]=")"
                else:
                    stack.append(")")
                    ret+=1
            else:
                if stack[-1]==")":
                    ret+=1
                    stack.pop()
                stack.append("(")
        while stack:
            top=stack.pop()
            if top=="(":
                ret+=2
        return ret