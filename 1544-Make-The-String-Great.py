class Solution:
    def makeGood(self, s: str) -> str:
        stack=[""]
        for item in s:
            top=stack[-1]
            if top!=item and item.lower()==top.lower():
                stack.pop()
            else:
                stack.append(item)
        return "".join(stack)