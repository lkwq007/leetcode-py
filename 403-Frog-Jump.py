class Solution:
    def canCross(self, stones: List[int]) -> bool:
        record={}
        for item in stones:
            record[item]=[]
        queue=[(0,0)]
        last=stones[-1]
        while queue:
            target=[]
            for pos,jump in queue:
                for next in range(jump-1,jump+2):
                    if pos+next==last:
                        return True
                    if pos+next in record and next not in record[pos+next]:
                        record[pos+next].append(next)
                        target.append((pos+next,next))
            queue=target
        return False