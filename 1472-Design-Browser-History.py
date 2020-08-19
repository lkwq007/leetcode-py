class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_stack=[]
        self.forward_stack=[]
        self.current=homepage

    def visit(self, url: str) -> None:
        self.forward_stack=[]
        self.back_stack.append(self.current)
        self.current=url

    def back(self, steps: int) -> str:
        tmp=self.current
        self.forward_stack.append(self.current)
        total=min(len(self.back_stack),steps)
        for i in range(total):
            tmp=self.back_stack.pop()
            self.forward_stack.append(tmp)
        self.forward_stack.pop()
        self.current=tmp
        return tmp
        
    def forward(self, steps: int) -> str:
        tmp=self.current
        self.back_stack.append(self.current)
        total=min(len(self.forward_stack),steps)
        for i in range(total):
            tmp=self.forward_stack.pop()
            self.back_stack.append(tmp)
        self.back_stack.pop()
        self.current=tmp
        return tmp


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)