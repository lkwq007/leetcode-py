class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        values.sort(key=lambda x:-x)
        total=0
        cnt=0
        for idx in range(len(values)):
            