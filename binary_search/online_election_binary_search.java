// [0, 5]
// l 1, r 2

// l 1 r 1

// [0,2,3,5]
// l 1, r 4
// l 3, r 4

// l 3, r 3

class TopVotedCandidate {
    List<Vote> A;

    public TopVotedCandidate(int[] persons, int[] times) {
        A = new ArrayList();
        Map<Integer, Integer> count = new HashMap();
        int leader = -1; // current leader
        int m = 0; // current number of votes for leader

        for (int i = 0; i < persons.length; ++i) {
            int p = persons[i], t = times[i];
            int c = count.getOrDefault(p, 0) + 1;
            count.put(p, c);

            if (c >= m) {
                if (p != leader) { // lead change
                    leader = p;
                    A.add(new Vote(leader, t));
                }

                if (c > m)
                    m = c;
            }
        }
    }

    // [0,5] 6
    // l 0, r 1
    // l 1 r 1

    // [0, 5, 6, 7]
    // l 0, r 3
    // l 0, r 1
    // l 1, r 1
    // l1, r0

    public int q(int t) {
        int l = 0, r = A.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (A.get(mid).time == t)
                return A.get(mid).person;
            if (A.get(mid).time < t)
                l = mid + 1;
            else
                r = mid - 1;
        }

        return A.get(r).person;
    }
}

class Vote {
    int person, time;

    Vote(int p, int t) {
        person = p;
        time = t;
    }
}