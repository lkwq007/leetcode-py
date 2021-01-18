class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth=0
        for cmd in logs:
            if cmd=="./":
                continue
            elif cmd=="../":
                if depth>0:
                    depth-=1
            else:
                depth+=1
        return depth