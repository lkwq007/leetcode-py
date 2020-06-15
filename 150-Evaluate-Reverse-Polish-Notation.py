class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+":
                tmp=stack.pop()
                stack[-1]+=tmp
            elif token=="-":
                tmp=stack.pop()
                stack[-1]-=tmp
            elif token=="*":
                tmp=stack.pop()
                stack[-1]*=tmp
            elif token=="/":
                tmp=stack.pop()
                stack[-1]=int(stack[-1]/tmp)
            else:
                stack.append(int(token))
        return stack[-1]