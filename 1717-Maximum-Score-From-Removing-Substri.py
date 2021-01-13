class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedy
        stack=[]
        ret=0
        first="a" if x>y else "b"
        second="b" if x>y else "a"
        score=max(x,y)
        rest=min(x,y)
        for item in s:
            if stack and stack[-1]==first and item==second:
                stack.pop()
                ret+=score
            else:
                stack.append(item)
        lst=stack
        stack=[]
        for item in lst:
            if stack and stack[-1]==second and item==first:
                stack.pop()
                ret+=rest
            else:
                stack.append(item)
        return ret


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedy
        stack=[]
        ret=0
        if x==y:
            for item in s:
                if stack and ((stack[-1]=="a" and item=="b") or (stack[-1]=="b" and item=="a")):
                    stack.pop()
                    ret+=x
                else:
                    stack.append(item)
            return ret
        first="a" if x>y else "b"
        second="b" if x>y else "a"
        score=max(x,y)
        rest=min(x,y)
        for item in s:
            if stack and stack[-1]==first and item==second:
                stack.pop()
                ret+=score
            else:
                stack.append(item)
        lst=stack
        stack=[]
        for item in lst:
            if stack and stack[-1]==second and item==first:
                stack.pop()
                ret+=rest
            else:
                stack.append(item)
        return ret