class Solution:
    def lastRemaining(self, n: int) -> int:
        if n==1:
            return 1
        # assume 0 - (n-1)
        end=n-1
        lst=[]
        step=0
        while end>1:
            if step&1:
                # tail
                lst.append(end&1)
            else:
                # head
                lst.append(1)
            end=end>>1
        acc=0
        lst.append(end)
        print(lst[::-1])
        for item in lst[::-1]:
            acc=acc*2+item
        return acc+1