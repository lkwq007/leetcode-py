class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        score=[0,0]
        lst=[(a,b) for a,b in zip(aliceValues,bobValues)]
        lst.sort(key=lambda x:-(x[0]+x[1]))
        for i in range(len(lst)):
            score[i&1]+=lst[i][i&1]
        if score[0]==score[1]:
            return 0
        elif score[0]>score[1]:
            return 1
        return -1
                

