class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst=[1]*(rowIndex+1)
        for i in range(1,rowIndex):
            first,second=lst[0],lst[1]
            for j in range(1,1+i):
                lst[j],first,second=first+second,lst[j],lst[j+1]
        return lst