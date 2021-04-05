class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        record={}
        for item in tiles:
            record[item]=record.get(item,0)+1
        def calc(x):
            ret=1
            while x>1:
                ret*=x
                x-=1
            return ret
        ret=calc(len(tiles))
        for _,val in record.items():
            ret=ret//calc(val)
        return ret