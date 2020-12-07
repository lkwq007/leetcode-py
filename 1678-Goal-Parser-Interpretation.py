class Solution:
    def interpret(self, command: str) -> str:
        ret=[]
        i=0
        while i<len(command):
            if command[i]=="G":
                ret.append("G")
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                ret.append("o")
                i+=2
            else:
                ret.append("al")
                i+=4
        return "".join(ret)