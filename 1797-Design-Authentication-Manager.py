class AuthenticationManager:
    # The values of currentTime across all the function calls will be strictly increasing.
    def __init__(self, timeToLive: int):
        self.record={}
        self.timeToLive=timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.record[tokenId]=currentTime+self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.record:
            return
        if currentTime<self.record[tokenId]:
            self.record[tokenId]=currentTime+self.timeToLive
        else:
            del self.record[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        for key in list(self.record.keys()):
            if self.record[key]<=currentTime:
                del self.record[key]
        return len(self.record)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)