class Solution:
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        for key in sorted(c.keys()):
            if count[key] > 0:
                for j in range(W)[::-1]:
                    count[key + j] -= count[key]
                    if count[key + j] < 0:
                        return False
        return True
