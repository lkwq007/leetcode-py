class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        stack=[]
        total=0
        for item in S:
            if item.isdigit():
                if stack:
                    stack[-1]*=int(item)
                    total*=int(item)
            else:
                stack.append()