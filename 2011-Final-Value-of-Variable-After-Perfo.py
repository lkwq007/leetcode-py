class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret=0
        for item in operations:
            if "-" in item:
                ret-=1
            else:
                ret+=1
        return ret