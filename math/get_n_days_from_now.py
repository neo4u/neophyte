class Solution:
    def get_date(n, date: tuple) -> tuple:
        d_to_m = {31: set([1, 3, 5, 7, 8, 10, 12]), 30: set([4, 6, 9, 11]), 28: set([2])}
        d, m, y = 0, 0, 0

        if d + date[0] > 30 or d + date[0] == 28:

