class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for item in ops:
            if item=="+":
                stack.append(stack[-2]+stack[-1])
            elif item=="D":
                stack.append(stack[-1]*2)
            elif item=="C":
                stack.pop()
            else:
                stack.append(int(item))
        return sum(stack)
