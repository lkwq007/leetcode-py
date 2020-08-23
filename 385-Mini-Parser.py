# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0]!="[":
            return NestedInteger(int(s))
        total=len(s)
        self.idx=0
        def digit():
            start=self.idx
            while self.idx<total and s[self.idx].isdigit():
                self.idx+=1
            return int(s[start:self.idx])
        stack=[]
        while self.idx<total:
            item=s[self.idx]
            if item=="[":
                lst=NestedInteger()
                stack.append(lst)
                self.idx+=1
            elif item=="]":
                top=stack.pop()
                if stack:
                    stack[-1].add(top)
                self.idx+=1
            elif item==",":
                self.idx+=1
            else:
                if item=="-":
                    self.idx+=1
                    num=-digit()
                elif item.isdigit():
                    num=digit()
                stack[-1].add(NestedInteger(num))
        return top