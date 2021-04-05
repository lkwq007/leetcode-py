class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter=ord(coordinates[0])-ord("a")
        num=int(coordinates[1])-1
        return bool((letter&1)^(num&1))