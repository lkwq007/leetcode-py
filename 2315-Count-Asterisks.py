class Solution:
    def countAsterisks(self, s: str) -> int:
        val=1
        ret=0
        for item in s:
            match item:
                case "|":
                    val=1-val
                case "*":
                    ret+=val
        return ret