// Keep an up to date record of every user's feed. The feed is immediately available when calling getNewsFeed.

// The feed for a user is updated whenever postTweet, follow or unfollow is called.

class Twitter {
    int globalTime;
    
    struct Tweet {
        Tweet (int id_, int time_) : id(id_), time(time_) {}
        int id;
        int time;
    };
    
    struct Followers {
        list<int> data; // linked list of followers
        unordered_map<int, list<int>::iterator> mapp; // map from followerId to iterator in linked list

        void add (int userId) {
            data.push_back(userId);
            mapp[userId] = prev(data.end());
        }

        void remove (int userId) {
            if (not contains(userId)) {
                return;
            }
            auto it = mapp[userId];
            data.erase(it);
            mapp.erase(userId);
        }

        const list<int>& get () {
            return data;
        }
        
        bool contains (int userId) {
            return mapp.find(userId) != mapp.end();
        }
    };

    struct Feed {
        list<Tweet*> data; // linked list of tweet pointers
        unordered_map<int, list<list<Tweet*>::iterator>> mapp; // map from followeeId to list of iterators to linked list
        
        void add_tweet (int userId, Tweet& tweet) {
            if (not contains(userId)) {
                return;
            }
            Tweet* topTweet = data.back();
            list<Tweet*>::iterator it;
            if (data.empty() or tweet.time > topTweet->time) {
                // just push to top
                data.push_back(&tweet);
                it = prev(data.end());
            } else {
                // new follow; must sort tweets
                it = lower_bound(data.begin(), data.end(), &tweet, [](Tweet* a, Tweet* b){
                    return a->time < b->time;
                });
                it = data.insert(it, &tweet);
            }
            // update map
            list<list<Tweet*>::iterator>& its = mapp[userId];
            its.push_back(it);
            while (its.size() > 10) {
                remove_first_tweet(its);
            }
        }
        
        void remove_first_tweet (list<list<Tweet*>::iterator>& its) {
            auto it = its.front();
            data.erase(it);
            its.pop_front();
        }
        
        void remove_followee (int userId) {
            if (not contains(userId)) {
                return;
            }
            list<list<Tweet*>::iterator>& its = mapp[userId];
            while (its.size()) {
                remove_first_tweet(its);
            }
            mapp.erase(userId);
        }
        
        void add_followee (int userId) {
            mapp[userId];
        }
        
        const list<Tweet*>& get () {
            return data;
        }
        
        bool contains (int userId) {
            return mapp.find(userId) != mapp.end();   
        }
    };
    
    struct User {
        deque<Tweet> tweets;
        Followers followers;
        Feed feed;
    };
    
    unordered_map<int, User> users;
    
public:
    /** Initialize your data structure here. */
    Twitter() {
        globalTime = 0;
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        User& user = users[userId];
        follow(userId, userId);

        // update tweets
        user.tweets.emplace_back(tweetId, globalTime++);
        Tweet& tweet = user.tweets.back();
        if (user.tweets.size() > 10) {
            user.tweets.pop_front();
        }
        // update feed for all followers
        const list<int>& followers = user.followers.get();
        for (auto it = followers.begin(); it != followers.end(); ++it) {
            int followerId = *it;
            User& follower = users[followerId];
            follower.feed.add_tweet(userId, tweet);
        }
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> res;
        if (users.find(userId) == users.end()) {
            return res;
        }
        User& user = users[userId];
        const list<Tweet*>& feed = user.feed.get();
        for (auto it = feed.rbegin(); it != feed.rend() and res.size() < 10; it++) {
            res.push_back((**it).id);
        }
        return res;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        User& followee = users[followeeId];
        User& follower = users[followerId];
        if (follower.feed.contains(followeeId)) {
            // already followed
            return;
        }
		// update followee
        followee.followers.add(followerId);
		// update follower's feed
        follower.feed.add_followee(followeeId);
        deque<Tweet>& tweets = followee.tweets;
        for (Tweet& tweet : tweets) {
            follower.feed.add_tweet(followeeId, tweet);
        }
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId or
            users.find(followerId) == users.end() or 
            users.find(followeeId) == users.end()) {
            return;
        }
        User& followee = users[followeeId];
        User& follower = users[followerId];
		// update followee
        followee.followers.remove(followerId);
		// update follower's feed
        follower.feed.remove_followee(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */