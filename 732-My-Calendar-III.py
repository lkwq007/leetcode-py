# at most 400 calls
class MyCalendarThree:

    def __init__(self):
        self.log=[]

    def book(self, start: int, end: int) -> int:
        acc=1
        ret=0
        for i in range(len(self.log)):
            s,e,_=self.log[i]
            if s<start<e or s<end<e or start<s<end or start<e<end:
                self.log[i][-1]+=1
                acc+=1
            ret=max(ret,self.log[i][-1])
        self.log.append([start,end,acc])
        return max(acc,ret)

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)