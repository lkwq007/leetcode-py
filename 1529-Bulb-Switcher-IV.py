class Solution:
    def minFlips(self, target: str) -> int:
        acc=0
        for i in range(len(target)):
            if target[i]=="0" and acc%2==0 or target[i]=="1" and acc%2==1:
                continue
            else:
                acc+=1
        return acc