class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapping=dict()
        for item in s:
            if item in mapping:
                mapping[item]=0
            else:
                mapping[item]=1
        for idx, item in enumerate(s,0):
            if mapping[item]:
                return idx
        return -1