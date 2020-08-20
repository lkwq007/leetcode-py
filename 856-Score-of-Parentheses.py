class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[0]
        for item in S:
            if item=="(":
                stack.append(0)
            else:
                top=stack.pop()
                if top==0:
                    stack[-1]+=1
                else:
                    stack[-1]+=top*2
        return stack[0]
                