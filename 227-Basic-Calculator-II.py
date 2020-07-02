class Solution:
    def calculate(self, s: str) -> int:
        precedence={"+":0,"-":0,"*":1,"/":1}
        expression="".join(s.split(" "))
        self.pos=0
        total=len(expression)
        def get_token():
            start=self.pos
            while self.pos<total and expression[self.pos].isdigit():
                self.pos+=1
            return int(expression[start:self.pos])
        func={
            "+": lambda x,y:x+y,
            "-": lambda x,y:x-y,
            "*": lambda x,y:x*y,
            "/": lambda x,y:x//y
        }
        total=len(expression)
        left=get_token()
        operand=[left]
        operator=None
        while self.pos<total:
            op=expression[self.pos]
            self.pos+=1
            right=get_token()
            if operator is None:
                operator=op
                operand.append(right)
            else:
                if precedence[op]>precedence[operator[-1]]:
                    operand[-1]=func[op](operand[-1],right)
                else:
                    operand[-2]=func[operator](operand[-2],operand[-1])
                    operand[-1]=right
                    operator=op
        if operator:
            return func[operator](operand[-2],operand[-1])
        else:
            return operand[-1]