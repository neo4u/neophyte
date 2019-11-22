from typing import List
import heapq


class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweet_map = {}
        self.follow_map = {}

    def postTweet(self, user, tweet):
        self.time += 1
        self.tweet_map[user] = self.tweet_map.get(user, []) + [(-self.time, tweet)]

    def getNewsFeed(self, user):
        h, tweets = [], self.tweet_map
        followers = self.follow_map.get(user, set()) | set([user])

        for p in followers:
            if p not in tweets or not tweets[p]: continue
            time, tweet = tweets[p][-1]
            h.append((time, tweet, p, len(tweets[p]) - 1))

        heapq.heapify(h)
        feed = []

        for _ in range(10):
            if not h: break
            time, tweet, person, idx = heapq.heappop(h)
            feed.append(tweet)
            if not idx: continue
            new_time, new_tweet = tweets[person][idx-1]
            heapq.heappush(h, (new_time, new_tweet, person, idx - 1))

        return feed

    def follow(self, follower, other):
        self.followee[follower] = self.follow_map.get(follower, set()) | set([other])

    def unfollow(self, follower, other):
        if follower not in self.followee: return
        self.follow_map[follower].discard(other)



# K is the number of followee of user.
# We have O(log(K)) runtime for getting news feed because we do maximum 10 extractions in a heap
# that holds maximum K elements (similar to what is done in merge K linked lists).
# The other ops are obviously O(1).

class Tweet:
    def __init__(self, id, time):
        self.id = id
        self.time = time


class Twitter:

    def __init__(self):
        self._global_time = 0
        self._id = 0
        self._time = 0






# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
