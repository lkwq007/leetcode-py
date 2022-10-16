class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for item in s:
            if item=="*" and stack and stack[-1]!="*":
                stack.pop()
            else:
                stack.append(item)
        return "".join(stack)