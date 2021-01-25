class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        acc=0
        ret=0
        for diff in gain:
            acc+=diff
            ret=max(acc,ret)
        return ret

import functools
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return functools.reduce(lambda x,y:(x[0]+y,max(x[0]+y,x[1])),gain,(0,0))[1]

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0,max(accumulate(gain)))