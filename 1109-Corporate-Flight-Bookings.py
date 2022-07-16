class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # line sweep
        lst=[0]*n
        for a,b,v in bookings:
            lst[a-1]+=v
            if b<n:
                lst[b]-=v
        for i in range(1,n):
            lst[i]+=lst[i-1]
        return lst


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # fenwick tree
        lst=[0]*(n+1)
        ret=[0]*n
        def update(pos,val):
            while pos<len(lst):
                lst[pos]+=val
                pos=pos|(pos+1)
        def query(pos):
            acc=0
            while pos>=0:
                acc+=lst[pos]
                pos=(pos&(pos+1))-1
            return acc
        for a,b,v in bookings:
            update(a,v)
            update(b+1,-v)
        for i in range(n):
            ret[i]=query(i+1)
        return ret