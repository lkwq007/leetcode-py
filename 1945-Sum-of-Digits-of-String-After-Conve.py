class Solution:
    def getLucky(self, s: str, k: int) -> int:
        base=ord("a")-1
        lst=[str(ord(item)-base) for item in s]
        cur="".join(lst)
        for i in range(k):
            acc=0
            for item in str(cur):
                acc+=int(item)
            cur=acc
        return cur
