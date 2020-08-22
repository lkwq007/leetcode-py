class Solution:
    def isValid(self, S: str) -> bool:
        if S[0]!="a":
            return False
        stack=["a"]
        for item in S[1:]:
            if item=="a":
                stack.append(item)
            elif item=="b":
                if stack and stack[-1]=="a":
                    stack[-1]="b"
                else:
                    return False
            else:
                if stack and stack[-1]=="b":
                    stack.pop()
                else:
                    return False
        return len(stack)==0