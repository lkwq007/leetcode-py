class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for idx, item in enumerate(nums, 0):
            rest = target - item
            if rest in map:
                return [map[rest], idx]
            else:
                map[item] = idx
        return []

