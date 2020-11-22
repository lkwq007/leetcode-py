class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        record={}
        record[keysPressed[0]]=releaseTimes[0]
        for i in range(1,len(keysPressed)):
            key=keysPressed[i]
            record[key]=max(record.get(key,0),releaseTimes[i]-releaseTimes[i-1])
        keys=sorted(record.keys())
        ret=keys[0]
        for key in keys:
            if record[ret]<=record[key]:
                ret=key
        return ret

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        acc=releaseTimes[0]
        key=keysPressed[0]
        for i in range(1,len(keysPressed)):
            time=releaseTimes[i]-releaseTimes[i-1]
            if acc<time or acc==time and key<keysPressed[i]:
                key=keysPressed[i]
                acc=time
        return key