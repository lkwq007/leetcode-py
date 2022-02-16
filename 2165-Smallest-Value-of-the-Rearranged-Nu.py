class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        val=num if num>0 else -num
        lst=[]
        while val>0:
            lst.append(val%10)
            val=val//10
        if num<0:
            lst.sort(key=lambda x:-x)
            acc=0
            for item in lst:
                acc*=10
                acc+=item
            return -acc
        lst.sort()
        zero=1
        acc=0
        for item in lst:
            if item==0:
                zero*=10
            else:
                acc*=10
                acc+=item
                acc*=zero
                zero=1
        return acc
        