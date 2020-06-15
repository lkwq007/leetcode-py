class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        stack=[]
        star=[]
        for idx,item in enumerate(s):
            if item==")":
                if stack or star:
                    if stack and stack[-1][0]=="(":
                        stack.pop()
                    else:
                        stack.append((item,idx))
                else:
                    return False
            elif item=="*":
                star.append(idx)
            else:
                stack.append((item,idx))
        mapping=[""]*len(s)
        for item,idx in stack:
            mapping[idx]=item
        for idx in star:
            mapping[idx]="*"
        new_s="".join(mapping)
        lst=list(new_s)
        idx=0
        # clear )
        while idx<len(lst):
            if idx>=0 and lst[idx]==")":
                if idx>0 and lst[idx-1]!=")":
                    del lst[idx]
                    del lst[idx-1]
                    idx=idx-1
                else:
                    return False
            else:
                idx+=1
        idx=len(lst)-1
        while idx>=0:
            if idx<len(lst) and lst[idx]=="(":
                if idx<len(lst)-1 and lst[idx+1]!="(":
                    del lst[idx+1]
                    del lst[idx]
                    idx=idx+1
                else:
                    return False
            else:
                idx-=1
        return True



x=Solution()
print(x.checkValidString("(*))"))
print(x.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        total=len(s)
        def valid(idx,stack):
            if idx<total:
                item=s[idx]
                if item=="(":
                    stack.append(item)
                    return valid(idx+1,stack)
                elif item==")":
                    if stack and stack[-1]=="(":
                        stack.pop()
                        return valid(idx+1,stack)
                    else:
                        return False
                else:
                    ret=valid(idx+1,stack[:])
                    if ret:
                        return ret
                    left_stack=stack[:]
                    left_stack.append("(")
                    ret=valid(idx+1,left_stack)
                    if ret:
                        return ret
                    right_stack=stack[:]
                    if right_stack and right_stack[-1]=="(":
                        right_stack.pop()
                        return valid(idx+1,right_stack)
                    else:
                        return False
            else:
                while stack:
                    item=stack.pop()
                    if item!="*":
                        return False
                return True
        return valid(0,[])

