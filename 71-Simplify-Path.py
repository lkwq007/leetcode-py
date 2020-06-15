class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs=path.split("/")
        stack=[]
        for item in dirs:
            if item:
                if item==".":
                    continue
                elif item=="..":
                    if stack: stack.pop()
                else:
                    stack.append(item)
        ret=""
        for item in stack:
            ret+="/"+item
        return ret if ret else "/"
