class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        record={}
        for item in logs:
            info=item.split(":")
            fid=int(info[0])
            op=info[1]
            time=int(info[2])
            if op=="start":
                if stack:
                    top=stack[-1]
                    top[1]+=time-top[2]
                    top[2]=time
                stack.append([fid,0,time])
            else:
                tmp=stack.pop()
                tmp[1]+=time-tmp[2]+1
                if tmp[0] in record:
                    record[tmp[0]]+=tmp[1]
                else:
                    record[tmp[0]]=tmp[1]
                if stack:
                    stack[-1][2]=time+1
        key=list(record.keys())
        key.sort()
        return list(map(lambda k:record[k],key))
