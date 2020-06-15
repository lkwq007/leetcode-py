# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.buffer=[]
        def dfs(lst,buffer):
            for item in lst:
                if item.isInteger():
                    buffer.append(item.getInteger())
                else:
                    dfs(item.getList(),buffer)
        dfs(nestedList,self.buffer)
        self.len=len(self.buffer)
        self.cursor=0
    
    def next(self) -> int:
        tmp=self.buffer[self.cursor]
        self.cursor+=1
        return tmp
    
    def hasNext(self) -> bool:
         return self.cursor<self.len
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())