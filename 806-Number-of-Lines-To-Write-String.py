class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=0
        acc=0
        base=ord("a")
        for item in s:
            c=ord(item)-base
            if acc+widths[c]<=100:
                acc+=widths[c]
            else:
                lines+=1
                acc=widths[c]
        return [lines,acc]