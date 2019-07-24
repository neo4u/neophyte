from heapq import heapify, heappop, heappush

# Amazon: Encoded file merge
def minimumTime(numOfSubFiles, files):
    heapify(files)
    time = 0

    while numOfSubFiles >= 2:
        first, second = [heappop(files) for _ in range(2)]
        sum_time = first + second
        time += sum_time
        heappush(files, sum_time)
        numOfSubFiles -= 1

    return time

assert minimumTime(4, [8, 4, 6, 12]) == 58
