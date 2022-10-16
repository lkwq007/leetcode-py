class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        record={}
        import itertools
        for v,w in itertools.chain(items1,items2):
            record[v]=record.get(v,0)+w
        return sorted([[k,v] for k,v in record.items()])