class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder=="#":
            return True
        stack=[]
        lst=preorder.split(",")
        for token in lst:
            if token=="#":
                stack.append(True)
            else:
                stack.append(False)
            while len(stack)>2 and stack[-1] and stack[-2]:
                stack.pop()
                stack.pop()
                if stack[-1]:
                    return False
                stack[-1]=True
        return stack[0] and len(stack)==1

x=Solution()
print(x.isValidSerialization("#,3,4,#,#,1,#,#,2,#,6,#,#"))