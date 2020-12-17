class Solution:
    def minPartitions(self, n: str) -> int:
        ret="0"
        for item in n:
            ret=max(ret,item)
        return int(ret)

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))