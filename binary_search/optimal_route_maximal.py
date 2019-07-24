from bisect import bisect

def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    returnRouteList.sort(key=lambda x: x[1])
    print(returnRouteList)
    ids_r, dists_r = list(map(list, zip(*returnRouteList)))
    result, curr_optimal, n = [], 0, len(returnRouteList)

    for id_f, dist_f in forwardRouteList:
        if dist_f == maxTravelDist: continue

        diff = maxTravelDist - dist_f
        i = bisect(dists_r, diff)
        if i == 0: continue

        if i <= n - 1 and dists_r[i] == diff:
            result.append([id_f, ids_r[i]])
        elif i > n - 1 or dists_r[i] > diff:
            i -= 1

        id_r, dist_r = returnRouteList[i]
        curr_sum = dist_f + dist_r
        if curr_sum > curr_optimal:
            curr_optimal = curr_sum
            result = [[id_f, id_r]]
        elif curr_sum == curr_optimal:
            result.append([id_f, id_r])
        print(f"result: {result} | curr_optimal: {curr_optimal}")

    return result

assert optimalUtilization(11000, [(1, 3000), (2, 5000), (3, 4000), (4, 10000)], [(1, 2000), (2, 3000), (3, 4000)]) == [[2, 3]]
assert optimalUtilization(
    10,
    [(1, 3), (2, 5), (3, 5), (4, 10)],
    [(1, 2), (2, 3), (3, 4)]
) == [[2, 3], [3, 3]]
assert optimalUtilization(
    20,
    [(1, 8), (2, 15), (3, 9)],
    [(1, 8), (2, 11), (3, 12)]
) == [[1, 3], [3, 2]]
assert optimalUtilization(
    7000,
    [(1, 2000), (2, 4000), (3, 6000)],
    [(1, 2000)]
) == [[2, 1]]
assert optimalUtilization(
    10000,
    [(1, 3000), (2, 5000), (3, 7000), (4, 10000)],
    [(1, 2000), (2, 3000), (3, 4000), (4, 5000)]
) == [[2, 4], [3, 2]]