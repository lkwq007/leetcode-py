class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst=list(range(len(heights)))
        lst.sort(key=lambda x:-heights[x])
        return [names[i] for i in lst]