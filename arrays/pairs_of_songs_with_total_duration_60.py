import collections

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts, result = collections.Counter([t % 60 for t in time]), 0

        for k in counts:
            if k == 0 or k == 30:
                result += counts[k] * (counts[k] - 1) // 2
            elif k < 30:
                result += counts[k] * counts[60 - k]

        return result


# Analysis
# From combination perspective:
# # pais to make up 60 = (# of time who % 60 = i) * (# of time who % 60 = 60 - i) for all possible i

# For example:
# If we have 5 numbers who % 60 = 20, and 7 numbers who % 60 = 40, then we can get 5 * 7 = 35 pairs to make up 60.

# Above all, if we represents the number of number who % 60 = i as map[i], then the result =

# map[0]? + // why ? explain below
# map[1] * map[59] +
# map[2] * map[58] +
# map[3] * map[57] +
# ... +
# map[28] * map[32] +
# map[29] * map[31] +
# map[30]? // why ? explain below
# Notice that I write map[0]? and map[30]? for the above formula. Because for map[0] and map[30], they are self-pairing to make up 60, so:

# map[0]? = C(n, 2) = map[0] * (map[0] - 1)/2
# map[30]? = C(n, 2) = map[30] * (map[30] - 1)/2


# Thus, final formula:
# map[0] * (map[0] - 1)/2 +
# map[1] * map[59] +
# map[2] * map[58] +
# map[3] * map[57] +
# ... +
# map[28] * map[32] +
# map[29] * map[31] +
# map[30] * (map[30] - 1)/2