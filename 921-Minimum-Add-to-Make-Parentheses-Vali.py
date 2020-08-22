class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack=[""]
        ret=0
        for item in S:
            if item==")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    ret+=1
            else:
                stack.append("(")
        while stack:
            top=stack.pop()
            if top=="(":
                ret+=1
        return ret