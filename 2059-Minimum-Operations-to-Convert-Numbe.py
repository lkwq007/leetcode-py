class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        record={start:0}
        if start==goal:
            return 0
        queue=[start]
        while queue:
            target=[]
            for item in queue:
                for num in nums:
                    for next in [item+num,item-num,item^num]:
                        if next==goal:
                            return record[item]+1
                        if 0<=next<=1000:
                            if next not in record:
                                record[next]=record[item]+1
                                target.append(next)
            queue=target
        return -1                            
                        