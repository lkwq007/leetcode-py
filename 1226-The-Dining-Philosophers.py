import threading
class DiningPhilosophers:
    def __init__(self):
        self.fork=[]
        for i in range(5):
            self.fork.append(threading.Lock())
        self.lock=threading.Lock()
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left=philosopher
        right=(philosopher+1)%5
        if philosopher%2==1:
            self.fork[left].acquire()
            self.fork[right].acquire()
            pickLeftFork()
            pickRightFork()
            eat()
            putRightFork()
            self.fork[right].release()
            putLeftFork()
            self.fork[left].release()
        else:
            self.fork[right].acquire()
            self.fork[left].acquire()
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            self.fork[left].release()
            putRightFork()
            self.fork[right].release()