import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n==1:
            return 1
        queue=primes[:]
        heapq.heapify(queue)
        record={item:1 for item in primes}
        cnt=1
        while cnt<n:
            top=heapq.heappop(queue)
            for item in primes:
                tmp=top*item
                if tmp not in record:
                    heapq.heappush(queue,top*item)
                    record[tmp]=1
            cnt+=1
        return top


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n==1:
            return 1
        lst=[1]
        idx=[0]*len(primes)
        for i in range(1,n):
            min_idx=0
            for j in range(len(primes)):
                if primes[j]*lst[idx[j]]<primes[min_idx]*lst[idx[min_idx]]:
                    min_idx=j
            cur=primes[min_idx]*lst[idx[min_idx]]
            lst.append(cur)
            for j in range(len(primes)):
                if primes[j]*lst[idx[j]]==cur:
                    idx[j]+=1
        return lst[-1]
