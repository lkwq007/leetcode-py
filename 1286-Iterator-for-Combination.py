class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # characters, sorted distinct
        self.char=characters
        self.last=len(characters)-combinationLength
        self.total=len(characters)
        self.idx=list(range(combinationLength))
    
    def next(self) -> str:
        ret=""
        for i in self.idx:
            ret+=self.char[i]
        for pos in range(0,len(self.idx)):
            if self.idx[~pos]<self.total+(~pos):
                self.idx[~pos]+=1
                break
            else:
                


    def hasNext(self) -> bool:
        return self.idx[0]!=self.last


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()