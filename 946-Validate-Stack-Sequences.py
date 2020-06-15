class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx1=0
        idx2=0
        stack=[]
        total=len(popped)
        while idx2<total:
            while len(stack)<1 or stack[-1]!=popped[idx2]:
                stack.append(pushed[idx1])
                idx1+=1
            if stack[-1]==popped[idx2]:
                stack.pop()
                idx2+=1
            if idx2<total and idx1>=total:
                return False
        return True