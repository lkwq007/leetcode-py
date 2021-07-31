class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n<3:
            return list(range(1,n+1))
        # even + odd, then num can only appear in one part
        lst=[]
        for i in range(2,n+1,2):
            if i%2==0:
                lst.append(i)
            else:
                lst.insert(0,i)
        lst2=[]
        for i in range(1,n+1,2):
            if i%2==0:
                lst2.append(i)
            else:
                lst2.insert(0,i)
        return lst+lst2

