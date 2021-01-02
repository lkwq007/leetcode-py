class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ret=0
        stack=[("",-1)]
        lst=input.split("\n")
        for item in lst:
            start=0
            while item[start]=="\t":
                start+=1
            name=item[start:]
            while start<=stack[-1][1]:
                stack.pop()
            if start>stack[-1][1]:
                if "." in name:
                    ret=max(ret,len(stack[-1][0])+len(name))
                else:
                    stack.append((stack[-1][0]+name+"/",start))
            else:

                if "." in name:
                    ret=max(ret,len(stack[-1][0])+len(name))
                else:
                    stack.append((stack[-1][0]+name+"/",start))
        return ret


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ret=0
        stack=[("",-1)]
        lst=input.split("\n")
        for item in lst:
            start=0
            while item[start]=="\t":
                start+=1
            name=item[start:]
            if start>stack[-1][1]:
                if "." in name:
                    ret=max(ret,len(stack[-1][0])+len(name))
                else:
                    stack.append((stack[-1][0]+name+"/",start))
            else:
                while start<=stack[-1][1]:
                    stack.pop()
                if "." in name:
                    ret=max(ret,len(stack[-1][0])+len(name))
                else:
                    stack.append((stack[-1][0]+name+"/",start))
        return ret