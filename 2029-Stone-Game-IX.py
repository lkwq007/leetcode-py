class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        record=[0]*3
        for item in stones:
            record[item%3]+=1
        while record[1]>0 and record[2]>0:
            if record[1]>record[2]:
                
        import functools
        @functools.lru_cache(None)
        def check(lst,bob=False):
            if sum(lst)==0:
                return False
            if lst[1]==0 and lst[2]==0:
                return bob
            
            
            
        
        return False