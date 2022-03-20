class Solution:
    def countCollisions(self, directions: str) -> int:
        stack=[directions[0]]
        ret=0
        for item in directions[1:]:
            if item=="L" and stack[-1]!="L":
                top=stack.pop()
                if top=="R":
                    ret+=2
                elif top=="S":
                    ret+=1
                cur="S"
                while stack and stack[-1]=="R":
                    stack.pop()
                    ret+=1
                stack.append(cur)
            elif item=="S" and stack[-1]=="R":
                while stack and stack[-1]=="R":
                    stack.pop()
                    ret+=1
                stack.append(item)
            else:
                stack.append(item)
        # print(stack)
        return ret
                
                