class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[""]
        for item in s:
            if item=="(":
                stack.append("")
            elif item==")":
                top=stack.pop()
                stack[-1]+=top[::-1]
            else:
                stack[-1]+=item
        return stack[0]