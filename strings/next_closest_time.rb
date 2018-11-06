# @param {String} time
# @return {String}
def next_closest_time(time)
    ans = start = 60 * time[0...2].to_i + time[3...time.size].to_i # in mins
    elapsed = 24 * 60
    allowed = time.chars.select { |c| c.to_i if c != ':' }.map(&:to_i)

    allowed.repeated_permutation(4).each do |h1, h2, m1, m2|
        hours, mins = 10 * h1 + h2, 10 * m1 + m2

        # Skip values where the values is not a valid time stamp like 8 can occur in 2nd mins place but can't occur in hours place
        next if hours >= 24 || mins >= 60
        curr = hours * 60 + mins

        # This value is always +ve and hence gives us the nearest value on both sides
        # this value is our main selection criteria
        mins_elapsed = (curr - start) % (24 * 60)
        if mins_elapsed.between?(1, elapsed - 1)
            ans = curr
            elapsed = mins_elapsed
        end
    end

    hh, mm = ans.divmod(60)
    "#{"%02d" % hh}:#{"%02d" % mm}"
end


# We have up to 4 different allowed digits, which naively gives us 4 * 4 * 4 * 4 possible times.
# For each possible time, let's check that it can be displayed on a clock:
# ie., hours < 24 and mins < 60.
# The best possible time != start is the one with the smallest cand_elapsed = (time - start) % (24 * 60),
# as this represents the time that has elapsed since start,
# and where the modulo operation is taken to be always non-negative.
# For example, if we have start = 720 (ie. noon),
# then times like 12:05 = 725 means that (725 - 720) % (24 * 60) = 5 seconds have elapsed;
# while times like 00:10 = 10 means that (10 - 720) % (24 * 60) = -710 % (24 * 60) = 730 seconds have elapsed.

# Also, we should make sure to handle cand_elapsed carefully.
# When our current candidate time cur is equal to the given starting time,
# then cand_elapsed will be 0 and we should handle this case appropriately.

# 681. Next Closest Time
# https://leetcode.com/problems/next-closest-time/

# Complexity Analysis
# Time Complexity: O(1). We all 4^4 possible times and take the best one.
# Space Complexity: O(1).