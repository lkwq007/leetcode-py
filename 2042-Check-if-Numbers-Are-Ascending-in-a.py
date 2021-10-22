class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        acc=-1
        for item in s.split(" "):
            if item[0].isdigit():
                val=int(item)
                if val<=acc:
                    return False
                acc=val
        return True