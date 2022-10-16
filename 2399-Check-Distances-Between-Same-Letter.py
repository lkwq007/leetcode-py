class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        record=[-1]*26
        base=ord("a")
        for i,item in enumerate(s):
            cur=ord(item)-base
            if record[cur]!=-1 and record[cur]+distance[cur]+1!=i:
                return False
            record[cur]=i
        return True
