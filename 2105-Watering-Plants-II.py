class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        acc0=capacityA
        acc1=capacityB
        ret=0
        for i in range((len(plants)+1)//2):
            if i==len(plants)-i-1:
                if acc0>=acc1 and acc0<plants[i]:
                    ret+=1
                if acc0<acc1 and acc1<plants[i]:
                    ret+=1
            else:
                if acc0>=plants[i]:
                    acc0-=plants[i]
                else:
                    acc0=capacityA-plants[i]
                    ret+=1
                if acc1>=plants[len(plants)-i-1]:
                    acc1-=plants[len(plants)-i-1]
                else:
                    acc1=capacityB-plants[len(plants)-i-1]
                    ret+=1
        return ret