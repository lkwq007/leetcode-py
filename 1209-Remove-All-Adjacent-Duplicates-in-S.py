class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[["",0]]
        for item in s:
            top=stack[-1]
            if item==top[0]:
                stack[-1][1]+=1
            else:
                stack.append([item,1])
            if stack[-1][1]==k:
                stack.pop()
        return "".join(map(lambda x:x[0]*x[1],stack))
            