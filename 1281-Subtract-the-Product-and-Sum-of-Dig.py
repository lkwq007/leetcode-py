class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        import functools
        lst=list(map(int,str(n)))
        return functools.reduce(lambda x,y:x*y,lst)-functools.reduce(lambda x,y:x+y,lst)
        