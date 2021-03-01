class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # simulate
        idx1,idx2=0,0
        total=len(pushed)
        stack=[-1]
        while idx2<total:
            while stack[-1]!=popped[idx2]:
                if idx1>=total:
                    return False
                stack.append(pushed[idx1])
                idx1+=1
            stack.pop()
            idx2+=1
        return True