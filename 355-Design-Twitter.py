class Twitter:

    def __init__(self):
        self.tweet=[]
        self.graph={}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet.append((userId,tweetId))
        # self.time+=1
        # if userId not in self.tweet:
        #     self.tweet[userId]=[]
        # self.tweet[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ret=[]
        cnt=0
        lst=self.graph.get(userId,[])
        for i in range(len(self.tweet)-1,-1,-1):
            uid,tid=self.tweet[i]
            if uid==userId or uid in lst:
                ret.append(tid)
                cnt+=1
            if cnt==10:
                break
        return ret
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.graph:
            self.graph[followerId]={}
        self.graph[followerId][followeeId]=1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.graph and followeeId in self.graph[followerId]:
            del self.graph[followerId][followeeId]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)