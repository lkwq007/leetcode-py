class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ret=[]
        table=["a","b","c"]
        lst=[a,b,c]
        last=-1
        cnt=0
        while True:
            idx=0 if last!=0 else 1
            for i in range(3):
                if lst[i]>lst[idx]:
                    if last==i and cnt<2 or last!=i:
                        idx=i
            if lst[idx]==0:
                break
            ret.append(table[idx])
            lst[idx]-=1
            if idx==last:
                cnt+=1
            else:
                cnt=1
            last=idx
        return "".join(ret)