class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        ret=0
        for item in heights:
            if stack:
                if item>stack[-1][0]:
                    stack.append((item,1))
                    ret=max(ret,item)
                else:
                    acc=1
                    while stack and stack[-1][0]>=item:
                        top,cnt=stack.pop()
                        acc+=cnt
                    ret=max(ret,item*acc)
                    stack.append((item,acc))
            else:
                ret=item
                stack.append((item,1))
        return ret

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def check(flag=False):
            stack=[]
            ret=0                
            for item in heights if flag else reversed(heights):
                if stack:
                    if item>stack[-1][0]:
                        stack.append((item,1))
                        ret=max(ret,item)
                    else:
                        acc=1
                        while stack and stack[-1][0]>=item:
                            top,cnt=stack.pop()
                            ret=max(top*(cnt+acc-1),ret)
                            acc+=cnt
                            
                        ret=max(ret,item*acc)
                        stack.append((item,acc))
                else:
                    ret=item
                    stack.append((item,1))
            return ret
        return max(check(),check(True))