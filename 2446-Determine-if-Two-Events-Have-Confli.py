class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0]<=event2[0]<=event1[1] or event2[0]<=event1[0]<=event2[1]