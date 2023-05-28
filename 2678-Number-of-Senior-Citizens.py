class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([item for item in details if int(item[-4:-2])>60])