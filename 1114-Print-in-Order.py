import threading
class Foo:
    def __init__(self):
        self.cond1=threading.Condition()
        self.cond2=threading.Condition()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.cond1:
        # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.cond1.notifyAll()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.cond1:
        # printSecond() outputs "second". Do not change or remove this line.
            self.cond1.wait()
            printSecond()
            with self.cond2:
                self.cond2.notifyAll()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.cond2:
        # printThird() outputs "third". Do not change or remove this line.
            printThird()