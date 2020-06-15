class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # constant space
        idx1=len(S)-1
        skip1=0
        idx2=len(T)-1
        skip2=0
        while idx1>=0 or idx2>=0:
            if S[idx1]=="#":
                skip1

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s=[]
        stack_t=[]
        def process(s):
            stack=[]
            for item in s:
                if item=="#":
                    if len(stack)>0:
                        stack.pop()
                else:
                    stack.append(item)
            return stack
        return process(S)==process(T)
