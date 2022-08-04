import threading
class Foo:
    def __init__(self):
        self.cond1=threading.Condition()
        self.cnt=1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.cond1:
        # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.cnt+=1
            self.cond1.notifyAll()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.cond1:
        # printSecond() outputs "second". Do not change or remove this line.
            self.cond1.wait_for(lambda:self.cnt==2)
            printSecond()
            self.cnt+=1
            self.cond1.notifyAll()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.cond1:
            self.cond1.wait_for(lambda:self.cnt==3)
            printThird()
            # printThird() outputs "third". Do not change or remove this line.
            # self.cond2.wait()
