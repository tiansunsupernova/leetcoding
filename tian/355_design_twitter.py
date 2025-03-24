class Twitter:

    def __init__(self):
        self.tweets = {}
        self.cnt = 1
        self.follows = defaultdict(set)  # k = followerId, v = set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque()
        self.tweets[userId].appendleft((self.cnt, tweetId))
        self.cnt += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        followees = self.follows[userId]

        h = []
        
        for followee in followees:
            if followee in self.tweets:
                news = self.tweets[followee]
                for i in range(min(len(news), 10)):
                    key, tweetId = news[i]
                    heapq.heappush(h, (-key, tweetId))
        
        res = []
        while h and len(res) < 10:
            _, x = heapq.heappop(h)
            res.append(x)
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)