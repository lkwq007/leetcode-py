
import functools
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # brute force?
        def is_palindrome(x):
            total=len(x)
            for i in range(len(x)//2):
                if x[i]!=x[total-i-1]:
                    return False
            return True
        @functools.lru_cache(maxsize=None)
        def probe(x):
            if len(x)==1:
                return [(x,)]
            # ret=[tuple(list(x))]
            ret=set([])
            ret.add(tuple(list(x)))
            if is_palindrome(x):
                ret.add((x,))
            for i in range(1,len(x)):
                left=probe(x[:i])
                right=probe(x[i:])
                if len(left)>1 or len(right)>1:
                    for l in left:
                        for r in right:
                            ret.append(l+r)
            return ret
        return probe(s)

# import functools
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         # brute force?
#         def is_palindrome(x):
#             total=len(x)
#             for i in range(len(x)//2):
#                 if x[i]!=x[total-i-1]:
#                     return False
#             return True
#         @functools.lru_cache(maxsize=None)
#         def probe(x):
#             if len(x)==1:
#                 return [[x]]
#             ret=[list(x)]
#             if is_palindrome(x):
#                 ret.append([x])
#             for i in range(1,len(x)):
#                 left=probe(x[:i])
#                 right=probe(x[i:])
#                 if len(left)>1 or len(right)>1:
#                     for l in left:
#                         for r in right:
#                             ret.append(l+r)
#             return ret
#         return probe(s)
