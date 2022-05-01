class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # constant space
        idx1=len(S)-1
        idx2=len(T)-1
        skip1=0
        skip2=0
        while idx1>=0 or idx2>=0:
            if (idx1>=0 and S[idx1]=="#") or (idx2>=0 and T[idx2]=="#"):
                while idx1>=0 and S[idx1]=="#":
                    skip1+=1
                    idx1-=1
                while idx2>=0 and T[idx2]=="#":
                    skip2+=1
                    idx2-=1
            elif skip1>0 or skip2>0:
                while idx1>=0 and skip1>0 and S[idx1]!="#":
                    skip1-=1
                    idx1-=1
                if idx1<0:
                    skip1=0
                while idx2>=0 and skip2>0 and T[idx2]!="#":
                    skip2-=1
                    idx2-=1
                if idx2<0:
                    skip2=0
            else:
                if idx1<0 or idx2<0 or S[idx1]!=T[idx2]:
                    return False
                idx1-=1
                idx2-=1
        return True

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
