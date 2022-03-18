class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # All the values of heights are unique.
        ret=[0]*len(heights)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            acc=0
            while stack and stack[-1]<heights[i]:
                acc+=1
                stack.pop()
            if stack:
                acc+=1
            ret[i]=acc
            stack.append(heights[i])
        return ret