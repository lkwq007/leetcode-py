class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        self.idx=0
        def exp():
            item=expression[self.idx]
            self.idx+=1
            if item=="t":
                return True
            elif item=="f":
                return False
            elif item=="!":
                self.idx+=1
                ret=not exp()
                self.idx+=1
                return ret
            elif item=="&":
                self.idx+=1
                acc=exp()
                while expression[self.idx]!=")":
                    self.idx+=1
                    acc=exp() and acc 
                self.idx+=1
                return acc
            else:
                self.idx+=1
                acc=exp()
                while expression[self.idx]!=")":
                    self.idx+=1
                    acc=exp() or acc
                self.idx+=1
                return acc
        return exp()