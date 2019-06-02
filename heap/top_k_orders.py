# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
uber eats

restaraunt, food
"a", "apple"
"a", "orange"
"a", "apple"
"b", "apple"
"b", "banana"
"a", "banana"

top k selling food for each restaraunt.
"""

from heapq import heappush, heappop, nlargest
from collections import defaultdict, Counter

def process_logs(log_data):
    logs = log_data.split()

class RestaurantOrders():
    def __init__(self):
        self.result = {}
    
    def top_k_orders(self, log_data):
        order_map = defaultdict(list)
        logs = log_data.split("\n")

        for log in logs:
            if not log: continue
            restaurant, food = log.split(", ")
            order_map[restaurant].append(food)
    
        for restaurant in order_map.keys():
            counts = Counter(order_map[restaurant])
            heap = []
            for food, frequency in counts.items():
                heap.append((frequency, food))
            self.result[restaurant] = heap

    def find_top_k(self, restaraunt, k):
        return [item[1] for item in nlargest(k, self.result[restaraunt])]


check = RestaurantOrders()
check.top_k_orders(
"""
a, apple
a, orange
a, apple
b, apple
b, banana
a, banana
a, banana
a, apple
"""
)

assert check.find_top_k('a', 1) == ['apple']
assert check.find_top_k('a', 2) == ['apple', 'banana']
