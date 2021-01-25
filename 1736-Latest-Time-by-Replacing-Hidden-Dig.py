class Solution:
    def maximumTime(self, time: str) -> str:
        # list all possibilities
        ret=list(time)
        if ret[-1]=="?":
            ret[-1]="9"
        if ret[-2]=="?":
            ret[-2]="5"
        if ret[1]=="?":
            if ret[0]=="2" or ret[0]=="?":
                ret[1]="3"
                ret[0]="2"
            else:
                ret[1]="9"
        if ret[0]=="?":
            if ret[1]<="3":
                ret[0]="2"
            else:
                ret[0]="1"
        return "".join(ret)