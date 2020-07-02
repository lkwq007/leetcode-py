class Solution:
    def calculate(self, s: str) -> int:
        # note that all number are non-negative integers
        self.pos=0
        def white_space():
            # we can also preposs the s
            while s[self.pos]==" ":
                self.pos+=1
        def get_token():
            white_space()
            start=self.pos
            while s[self.pos].isdigit():
                self.pos+=1
            end=self.pos
            white_space()
            return int(s[start:end])
        def expr():
            white_space()
            