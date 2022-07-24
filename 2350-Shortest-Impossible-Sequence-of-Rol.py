class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        acc=set()
        ret=1
        for item in rolls:
            acc.add(item)
            if len(acc)==k:
                ret+=1
                acc=set()
        return ret

import functools
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        return functools.reduce(lambda acc,cur: (set(),acc[1]+1) if len((acc[0].add(cur),acc[0])[1])==k else acc,rolls,(set(),1))[1]