from typing import List
import math


class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        maxV, minV, errors = 0, 0, []

        # gather minV, maxV and errors
        for fp in map(float, prices):
            f, c = math.floor(fp), math.ceil(fp)
            minV, maxV = minV + f, maxV + c
            fError, cError = fp - f, c - fp
            errors.append((fError, cError))

        # lets make sure this is actually possible
        if target < minV or target > maxV: return "-1"

        # The number of prices that need to be rounded up (rest are rounded down)
        ceilCount = target - minV

        # Floor errors are enough to give us what we need
        errors = sorted(errors, reverse=True)

        #min error
        minError = sum(e[1] for e in errors[:ceilCount]) + sum(e[0] for e in errors[ceilCount:])

        # return the error
        return "{:.3f}".format(minError)


# CONDENSED
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        min_v, max_v, errors = 0, 0, []

        for price in map(float, prices):
            f, c = math.floor(price), math.ceil(price)
            min_v += f; max_v += c
            f_error, c_error = abs(price - f), abs(price - c)
            errors.append((f_error, c_error))

        if not min_v <= target <= max_v: return '-1'

        k = target - min_v
        errors = sorted(errors, reverse=True)

        result = sum(e[1] for e in errors[:k]) + sum(e[0] for e in errors[k:])
        return f"{result:.3f}"


# 1058. Minimize Rounding Error to Meet Target
# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/description/


# For each number, we have two choice: floor or ceil.
# So the minimum sum we could get is sum each floored price.
# And the maximum sum we could get is sum each ceiled price.
# If target is larger or equal than the minimum one and small or equal to the maximum one,
# we could get such value. Otherwise we need to return a "-1".

# If we can get target, we can do floor operation to each value first.
# Now we get a minimum value.
# To get the target, we need select (target - minimum) numbers of price and do ceil operation on it instead of floor operation so that we can get target.(ceil(p) - floor(p) = 1)
# We want to minimum the total change (which is sum of the abs change by doing operation(floor | ceil) to each price).
# So we can:

# - Calculate the change made by floor operation and ceil operation for each price.
# - Calculate the reduce in the change by filp the floor operation to ceil operation.
# - Sort them in des order.
# - For the first (target - minimum) changes, we filp floor operation to ceil.(As we gain more reduces to the total changes by doing ceil operation to these prices.)
# - For the rest changes, we select floor operation.
# - Return the sum of all changes.
