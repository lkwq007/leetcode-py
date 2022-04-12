class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        record={}
        def probe(lst,acc):
            record[acc]=1
            if len(lst)==0:
                return
            for i in range(len(lst)):
                cur=lst[i]
                probe(lst[:i]+lst[i+1:],acc+cur)
        probe(tiles,"")
        return len(record)-1