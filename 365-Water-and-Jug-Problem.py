class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity+jug2Capacity<targetCapacity:
            return False
        record={}
        def check(acc1,acc2):
            record[(acc1,acc2)]=1
            if targetCapacity in [acc1,acc2,acc1+acc2]:
                return True
            if targetCapacity>acc1 and (targetCapacity-acc1)%jug2Capacity==0:
                return True
            if targetCapacity>acc2 and (targetCapacity-acc2)%jug1Capacity==0:
                return True
            lst=[
                (acc1,jug2Capacity),
                (jug1Capacity,acc2),
                (0,acc2),
                (acc1,0),
                (min(acc1+acc2,jug1Capacity),max(0,acc2-(min(acc1+acc2,jug1Capacity)-acc1))),
                (max(0,acc1-(min(acc1+acc2,jug2Capacity)-acc2)),min(acc1+acc2,jug2Capacity))
            ]
            for x,y in lst:
                if (x,y) not in record:
                    if check(x,y):
                        return True
            return False
        return check(0,0)