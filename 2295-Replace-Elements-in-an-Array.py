class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mapping={item:item for item in nums}
        for u,v in operations:
            mapping[v]=mapping[u]
            del mapping[u]
        imapping={v:k for k,v in mapping.items()}
        return [imapping.get(item,item) for item in nums]
