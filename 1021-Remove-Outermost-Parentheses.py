class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ret=""
        depth=0
        for item in S:
            if item=="(":
                if depth>0:
                    ret+=item
                depth+=1
            else:
                depth-=1
                if depth>0:
                    ret+=item
        return ret