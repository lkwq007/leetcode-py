class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # ugly numbers primee factor only includes 2,3,5
        if n==1:
            return 1
        factor=[2,3,5]
        lst=[[1] for _ in range(3)]
        idx=[0]*3
        def find_min():
            ret=2
            for i in range(2):
                if factor[i]*lst[i][idx[i]]<factor[ret]*lst[ret][idx[ret]]:
                    ret=i
            return ret,factor[ret]*lst[ret][idx[ret]]
        last=0
        i=1
        while i<n:
            ret,num=find_min()
            idx[ret]+=1
            if num!=last:
                for j in range(3):
                    lst[j].append(num)
                i+=1
            last=num
        return num

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # ugly numbers primee factor only includes 2,3,5
        if n==1:
            return 1
        lst=[1]
        idx2=0
        idx3=0
        idx5=0
        for i in range(1,n):
            num2=lst[idx2]*2
            num3=lst[idx3]*3
            num5=lst[idx5]*5
            cur=min((num2,num3,num5))
            if cur==num2:
                idx2+=1
            if cur==num3:
                idx3+=1
            if cur==num5:
                idx5+=1
            lst.append(cur)
        return cur
x=Solution()
x.nthUglyNumber(10)