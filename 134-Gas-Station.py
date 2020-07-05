class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        acc=gas[:]
        lst=[]
        total_gas=0
        total_cost=0
        for idx in range(len(acc)):
            acc[idx]-=cost[idx]
            total_gas+=gas[idx]
            total_cost+=cost[idx]
            if acc[idx]>=0:
                lst.append(idx)
        if len(lst)<0 or total_gas<total_cost:
            return -1
        total=len(gas)
        for idx in lst:
            tank=0
            for i in range(0,total):
                j=(i+idx)%total
                tank+=acc[j]
                if tank<0:
                    break
            if tank>=0:
                return idx
        return -1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        acc=gas[:]
        total_gas=0
        total_cost=0
        start=-1
        for idx in range(len(acc)):
            acc[idx]-=cost[idx]
            total_gas+=gas[idx]
            total_cost+=cost[idx]
            if start<0:
                start=idx
        if start<0 or total_gas<total_cost:
            return -1
        total=len(gas)
        idx=start
        while idx<start+total:
            tank=0
            for i in range(0,total):
                j=(idx+i)%total
                tank+=acc[j]
                if tank<0:
                    break
            if tank>=0:
                return idx%total
            else:
                idx=idx+i+1
        return -1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=len(gas)
        idx=0
        start=-1
        while idx<total:
            if gas[idx]>=cost[idx]:
                start=idx
                break
            idx+=1
        if start<0:
            return -1
        idx=start
        while idx<start+total:
            tank=0
            for i in range(0,total):
                j=(idx+i)%total
                tank+=gas[j]-cost[j]
                if tank<0:
                    break
            if tank>=0:
                return idx%total
            else:
                idx=idx+i+1
        return -1