import threading
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cur=1
        self.cond=threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	for i in range(1,self.n+1):
            if i%3==0 and i%5!=0:
                with self.cond:
                    self.cond.wait_for(lambda:i==self.cur)
                    self.cur+=1
                    printFizz()
                    self.cond.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	for i in range(1,self.n+1):
            if i%3!=0 and i%5==0:
                with self.cond:
                    self.cond.wait_for(lambda:i==self.cur)
                    self.cur+=1
                    printBuzz()
                    self.cond.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n+1):
            if i%3==0 and i%5==0:
                with self.cond:
                    self.cond.wait_for(lambda:i==self.cur)
                    self.cur+=1
                    printFizzBuzz()
                    self.cond.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            if i%3!=0 and i%5!=0:
                with self.cond:
                    if i>1 and ((i-1)%3==0 or (i-1)%5==0):
                        self.cond.notify_all()
                        self.cond.wait_for(lambda:i==self.cur)
                    self.cur+=1
                    printNumber(i)
                    self.cond.notify_all()