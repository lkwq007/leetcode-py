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
            sign=1
            if self.pos<total and s[self.pos]=="-":
                self.pos+=1
                start+=1
                sign=-1
            while self.pos<total and s[self.pos].isdigit():
                self.pos+=1
            end=self.pos
            white_space()
            return int(s[start:end])*sign
        def expr():
            op="+"
            acc=0
            flag=True
            white_space()
            if self.pos<total and s[self.pos]=="-":
                op="-"
                self.pos+=1
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
            return acc
        return expr()