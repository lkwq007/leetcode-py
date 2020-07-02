class Solution:
    def calculate(self, s: str) -> int:
        # note that all number are non-negative integers
        self.pos=0
        total=len(s)
        def white_space():
            # we can also preposs the s
            while self.pos<total and s[self.pos]==" ":
                self.pos+=1
        def get_token():
            start=self.pos
            while self.pos<total and s[self.pos].isdigit():
                self.pos+=1
            end=self.pos
            white_space()
            return int(s[start:end])
        def expr():
            op="+"
            acc=0
            flag=True
            white_space()
            while self.pos<total and s[self.pos]!=")":
                if s[self.pos]=="(":
                    self.pos+=1
                    item=expr()
                else:
                    item=get_token()
                if op=="+":
                    acc+=item
                else:
                    acc-=item
                if self.pos<total and s[self.pos]!=")":
                    flag=False
                    op=s[self.pos]
                    self.pos+=1
                    white_space()
                if self.pos<total and s[self.pos]==")":
                    self.pos+=1
                    break
            white_space()
            return item if flag else acc
        return expr()

x=Solution()
print(x.calculate("1 + 1"))