class FrequencyTracker:

    def __init__(self):
        self.freq={}
        self.record={}

    def add(self, number: int) -> None:
        freq=self.record.get(number,0)
        if freq>0:
            self.freq[freq]-=1
        freq+=1
        self.record[number]=freq
        self.freq[freq]=self.freq.get(freq,0)+1


    def deleteOne(self, number: int) -> None:
        if number in self.record:
            freq=self.record[number]
            if freq==1:
                del self.record[number]
            else:
                self.freq[freq-1]=self.freq.get(freq-1,0)+1
                self.record[number]-=1
            self.freq[freq]-=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency,0)>0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)