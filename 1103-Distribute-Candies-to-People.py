from math import sqrt
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        stop=(sqrt(8*candies)-1)//2
        stop=int(stop)
        while stop*(stop+1)//2<=candies:
            stop+=1
        stop-=1
        pos=stop%num_people
        times=stop//num_people
        acc0=(times+1)*times//2*num_people
        num0=times+1
        acc1=0 if times==0 else (times-1)*times//2*num_people
        num1=0 if times==0 else times
        lst=[i*num0+acc0 if i<=pos else i*num1+acc1 for i in range(1,num_people+1)]
        rest=candies-stop*(stop+1)//2
        lst[pos]+=rest
        return lst