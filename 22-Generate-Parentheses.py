class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n<1:
            return [""]
        ret=[]
        def to_string():
            return ""
        def probe(node,acc):
            if acc==n:
                ret.append(to_string(node))
                return
            