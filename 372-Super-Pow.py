class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        term=1337
        acc=a%term
        ret=1
        for num in reversed(b):
            next=1
            # print(num)
            for i in range(10):
                next*=acc
                next%=term
                if i==num-1:
                    ret*=next
                    ret%=term
            acc=next
        return ret
