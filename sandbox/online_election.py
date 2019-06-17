import collections
import bisect


class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.events = []
        counts = collections.Counter()
        leader, max_votes = None, 0

        for p, t in zip(persons, times):
            counts[p] += 1
            c = counts[p]

            if c >= max_votes:
                if leader != p: self.events.append((t, p))
                leader, max_votes = p, c

    def q(self, t):
        i = bisect.bisect(self.events, (t, float("inf")))
        return self.events[i - 1][1]
