import heapq
class SORTracker:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
    
    def convert(self,name):
        lst=[]
        for item in (name+" "*10)[:10]:
            lst.append(chr(ord("z")-ord(item)+ord("a")))
        return "".join(lst)

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.minheap,(score,self.convert(name)))
        score,name=heapq.heappop(self.minheap)
        heapq.heappush(self.maxheap,(-score,self.convert(name)))


    def get(self) -> str:
        # print(self.idx,len(self.minheap),self.maxheap,self.minheap)
        ret=self.maxheap[0][-1]
        score,name=heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap,(-score,self.convert(name)))
        return ret.strip()

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()