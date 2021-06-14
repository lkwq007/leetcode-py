class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # brute force
        for i in range(left,right+1):
            flag=False
            for l,r in ranges:
                if l<=i<=r:
                    flag=True
            if not flag:
                return False
        return True

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # brute force
        record=[0]*51
        for l,r in ranges:
            for i in range(l,r+1):
                record[i]+=1
        for i in range(left,right+1):
            if record[i]==0:
                return False
        return True