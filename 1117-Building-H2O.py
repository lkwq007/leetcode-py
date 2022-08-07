import threading
class H2O:
    def __init__(self):
        self.end=threading.Lock()
        self.start=threading.Lock()
        self.cnt=0
        self.start.acquire()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.end.acquire()
        releaseHydrogen()
        self.cnt+=1
        if self.cnt%2==0:
            self.start.release()
        else:
            self.end.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.start.acquire()
        releaseOxygen()
        self.end.release()
        