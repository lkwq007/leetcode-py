class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        left="({["
        mapping={"{":"}","[":"]","(":")"}
        for item in s:
            if item in left:
                stack.append(item)
            else:
                if len(stack)<1:
                    return False
                tmp=stack.pop()
                if mapping[tmp]!=item:
                    return False
        if len(stack)==0:
            return True
        else:
            return False