class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # n<=6
        import functools
        @functools.lru_cache(None) 
        def probe(lst):
            ret=0
            for p,n in zip(price,lst):
                ret+=p*n
            for offer in special:
                flag=True
                for i in range(len(lst)):
                    if lst[i]<offer[i]:
                        flag=False
                        break
                if flag:
                    cur=offer[-1]+probe(tuple(lst[j]-offer[j] for j in range(len(lst))))
                    if cur<ret:
                        ret=cur
            return ret
        return probe(tuple(needs))