class MyCalendarThree(object):
    
    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active

        return ans


# MyCalendarThree();
# MyCalendarThree.book(10, 20); // returns 1
# MyCalendarThree.book(50, 60); // returns 1
# MyCalendarThree.book(10, 40); // returns 2
# MyCalendarThree.book(5, 15); // returns 3
# MyCalendarThree.book(5, 10); // returns 3
# MyCalendarThree.book(25, 55); // returns 3

# delta
# ----------
# 5: 1
# 10: 2
# 15: -1
# 20: -1
# 25: 1
# 40: -1
# 50: 1
# 55: -1
# 60: -1
