class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        record={}
        bulls=0
        cows=0
        for idx in range(len(secret)):
            if secret[idx]==guess[idx]:
                bulls+=1
            else:
                item=secret[idx]
                record[item]=record.get(item,0)+1
        for idx in range(len(guess)):
            item=guess[idx]
            if secret[idx]!=guess[idx] and item in record and record[item]>0:
                record[item]-=1
                cows+=1
        return str(bulls)+"A"+str(cows)+"B"