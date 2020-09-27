import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # non negative, so the length is given
        lst=[str(item) for item in nums]
        def compare(a,b):
            x=a+b
            y=b+a
            if x>y:
                return -1
            elif x<y:
                return 1
            return 0
        lst.sort(key=functools.cmp_to_key(compare))
        ret="".join(lst)
        for i in range(len(ret)):
            if ret[i]!="0":
                break
        return ret[i:]

# import functools
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         # non negative, so the length is given
#         lst=[str(item) for item in nums]
#         def compare(a,b):
#             for x,y in zip(a,b):
#                 if x<y:
#                     return 1
#                 elif x>y:
#                     return -1
#             if len(a)==len(b):
#                 return 0
#             elif len(a)<len(b):
#                 if b[len(a)]>a[0]:
#                     return 1
#                 return -1
#             else:
#                 if a[len(b)]>b[0]:
#                     return -1
#                 return 1
#         lst.sort(key=functools.cmp_to_key(compare))
#         ret="".join(lst)
#         for i in range(len(ret)):
#             if ret[i]!="0":
#                 break
#         return ret[i:]