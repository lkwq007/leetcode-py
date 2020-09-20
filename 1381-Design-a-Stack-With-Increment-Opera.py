# we simply record each increment, and then evaluate them lazily
# TODO: How about increment k element from the top of the stack?
# it seems to be different with this problems,
# however, it's actually a variant of this problems
# we can apply `increment(total,val) and increment(total-k,-val)`
class CustomStack:

    def __init__(self, maxSize: int):
        self.acc=[0]*maxSize
        self.stack=[0]*maxSize
        self.total=0
        self.length=maxSize

    def push(self, x: int) -> None:
        if self.total<self.length:
            self.stack[self.total]=x
            self.total+=1

    def pop(self) -> int:
        top=self.total-1
        if top<0:
            return -1
        self.total-=1
        acc=self.acc[top]
        if top>0:
            self.acc[top-1]+=acc
        self.acc[top]=0
        return self.stack[top]+acc

    def increment(self, k: int, val: int) -> None:
        cur=min(self.total,k)
        if cur>0:
            self.acc[cur-1]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)