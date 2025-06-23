class Twitter:

    # Space: O(N∗m+N∗M+n) where n is the total number of followeeIds associated with the userId, m is the maximum number of tweets by any user, N is the total number of userIds and M is the maximum number of followees for any user.
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId
        
    # Time: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        # Instead of maintaining an increasing timestamp and picking the max to determine the most recent tweet, we use a decrementing counter as python supports min heap only. So the tweet with min counter value will be the most recent.
        self.count -= 1

    # Time: O(nlogn)
    def getNewsFeed(self, userId: int) -> List[int]:
        # Stores tweetIds from most to least recent
        res = []
        minHeap = []
        # User should see his own tweets too
        self.followMap[userId].add(userId)
      
        # For every follower, get the last tweet added in the list and add it to the heap to get the most recent tweet across all followees
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # IMP: push followeeId and index to the heap too so when we pop this from the heap, we know which index to consider next time when we look at tweets from this followee
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Get upto 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # It means there are more tweets from this followee that we may want to consider in the next iteration
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
        

    # Time: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    # Time: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
