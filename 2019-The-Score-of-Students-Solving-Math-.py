import functools
class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        stack=[int(s[0])]
        pos=1
        while pos<len(s):
            if s[pos]=="+":
                stack.append(int(s[pos+1]))
            else:
                stack[-1]*=int(s[pos+1])
            pos+=2
        val=sum(stack)
        mapping=[0]*1001
        @functools.lru_cache(maxsize=None)
        def probe(lst):
            ret=set([])
            if len(lst)==1:
                return set([int(lst[0])])
            for i in range(1,len(lst),2):
                op=lst[i]
                left=probe(lst[:i])
                right=probe(lst[i+1:])
                for l in left:
                    for r in right:
                        if op=="+":
                            val=l+r
                        else:
                            val=l*r
                        if val<=1000:
                            ret.add(val)
            return ret
        for item in probe(s):
            if 0<=item<=1000:
                mapping[item]=2
        # probe.cache_clear()
        mapping[val]=5
        return sum([mapping[x] for x in answers])