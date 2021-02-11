class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        record={}
        quantity.sort(key=lambda x:-x)
        for item in nums:
            record[item]=record.get(item,0)+1
        def probe(idx):
            keys=list(record.keys())
            keys.sort(lambda x:-x)
            for key in keys:
                if record[key]>=quantity[idx]:
                    
        

