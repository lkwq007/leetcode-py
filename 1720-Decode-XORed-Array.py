class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret=[first]
        for item in encoded:
            val=item^first
            first=val
            ret.append(val)
        return ret

import itertools
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return list(itertools.accumulate([first]+encoded,lambda x,y:x^y))