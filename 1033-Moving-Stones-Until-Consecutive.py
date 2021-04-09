class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        lst=[a,b,c]
        lst.sort()
        max_val=lst[-1]-lst[0]-2
        min_val=2
        if max_val==0:
            min_val=0
        else:
            for i in range(2):
                if lst[i+1]<=lst[i]+2:
                    min_val-=1
                    break
        return [min_val,max_val]