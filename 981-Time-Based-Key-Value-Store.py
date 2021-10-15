class TimeMap:

    def __init__(self):
        self.record={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamps timestamp of set are strictly increasing.
        if key not in self.record:
            self.record[key]=[]
        self.record[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.record or timestamp<self.record[key][0][0]:
            return ""
        left=0
        right=len(self.record[key])-1
        while left<right:
            middle=left+(right-left)//2
            val=self.record[key][middle]
            if val[0]==timestamp:
                return val[1]
            elif val[0]<timestamp:
                left=middle+1
            else:
                right=middle
        while left>0 and self.record[key][left][0]>timestamp:
            left-=1
        return self.record[key][left][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)