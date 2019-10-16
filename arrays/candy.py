class Solution(object):
    def candy(self, ratings):
        candies = [1 for _ in range(len(ratings))]
        # flow 1 -> 
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # flow 2 <-
        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i - 1] = candies[i] + 1

        return sum(candies)


# 135. Candy
# https://leetcode.com/problems/candy/description/