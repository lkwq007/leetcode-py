class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        record={}
        for item in arr1:
            record[item]=record.get(item,0)+1
        head=[]
        for item in arr2:
            if item in record:
                for i in range(record[item]):
                    head.append(item)
                del record[item]
        for key in sorted(record.keys()):
            for i in range(record[key]):
                head.append(key)
        return head

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapping={}
        for i,item in enumerate(arr2,0):
            mapping[item]=i
        arr1.sort(key=lambda x: (mapping.get(x,len(arr2)),x))
        return arr1