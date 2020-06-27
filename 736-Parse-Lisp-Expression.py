class Solution:
    def evaluate(self, expression: str) -> int:
        # recursive descent parser
        self.pos=0
        self.env={}
        def next_token():
            start=self.pos
            while expression[self.pos]!=" " and expression[self.pos]!=")":
                self.pos+=1
            return expression[start:self.pos]
        def eat_space():
            while expression[self.pos]==" ":
                self.pos+=1
            return
        def eval():
            if expression[self.pos]=="(":
                self.pos+=1
                operator=next_token()
                if operator=="add":
                    eat_space()
                    a=eval()
                    eat_space()
                    b=eval()
                    ret=a+b
                elif operator=="mult":
                    eat_space()
                    a=eval()
                    eat_space()
                    b=eval()
                    ret=a*b
                else:
                    eat_space()
                    var_lst=[]
                    while True:
                        if not expression[self.pos].isalpha():
                            ret=eval()
                            break
                        else:
                            var=next_token()
                            if expression[self.pos]!=" ":
                                ret=self.env[var][-1]
                                break
                            eat_space()
                        var_lst.append(var)
                        val=eval()
                        if var in self.env:
                            self.env[var].append(val)
                        else:
                            self.env[var]=[val]
                        eat_space()
                    for var in var_lst:
                        self.env[var].pop()
                if expression[self.pos]==")":
                    self.pos+=1
                    return ret
            else:
                token=next_token()
                if token.isdigit() or token[0]=="-":
                    return int(token)
                else:
                    return self.env[token][-1]
        return eval()

x=Solution()
print(x.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"))
print(x.evaluate("(let x 7 -12)"))