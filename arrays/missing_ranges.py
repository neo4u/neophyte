class Solution:
    def findMissingRanges(self, A, lower, upper):
        result = []
        A.append(upper+1)
        prev = lower - 1

        for i in A:
            if (i - prev == 2):
                result.append(str(i - 1))
            elif (i - prev > 2):
                result.append(str(prev + 1) + "->" + str(i - 1))

            prev = i

        return result


# sam, 123, 4
# sai, 345, 20
# ram, 456, 25
# sai, 123, 30

# def asdfasdf(log):
#     logs = log.split('\n')
#     for l in logs:
#         name, num, ts = l.split(",")






# [0 5]
# 0 + 1, 5 - 1

# [10, 15, 100]

# 16 - 99

# 1,2,3