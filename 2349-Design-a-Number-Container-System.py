import heapq
class NumberContainers:

    def __init__(self):
        self.record={}
        self.idx={}

    def change(self, index: int, number: int) -> None:
        self.record[index]=number
        if number not in self.idx:
            self.idx[number]=[index]
        else:
            heapq.heappush(self.idx[number],index)

    def find(self, number: int) -> int:
        if number in self.idx:
            queue=self.idx[number]
            while queue:
                top=queue[0]
                if self.record.get(top,0)==number:
                    return top
                heapq.heappop(queue)
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)