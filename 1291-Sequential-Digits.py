class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def count(x):
            ret=0
            while x>0:
                ret+=1
                x=x//10
            return ret
        start=count(low)
        end=count(high)
        lst=[]
        def probe(i):
            total=i
            while i<=9:
                tmp=0
                for j in range(total):
                    tmp*=10
                    tmp+=i-total+j+1
                lst.append(tmp)
                i+=1
        for i in range(start,end+1):
            probe(i)
        return [item for item in lst if low<=item<=high]
