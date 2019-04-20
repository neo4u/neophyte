# @param {String[]} words
# @param {String} order
# @return {Boolean}
def is_alien_sorted(words, order)
    order_idx = Hash.new(0)
    order.each_char.with_index { |c, i| order_idx[c] = i }

    words.each_cons(2) do |w1, w2|
        m, n = w1.size, w2.size
        min, found_mismatch = [m, n].min, false
        0.upto(min - 1) do |i|
            c1, c2 = w1[i], w2[i]
            next if c1 == c2
            found_mismatch = true
            return false if order_idx[c1] > order_idx[c2]
            break
        end

        return false if !found_mismatch && m > n
    end

    true
end


# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/


# Steps:
# 1. Capture indices of the order string in a dictionary
# 2. Compare every two consecutive words using the steps below
#     - In every 2 words check for the smaller one and compare chars upto the min len
#     - At the first mismatch return false if w1's char appears after the w2's char
#     - We use the found variable to check if the loop exited due to finding mismatch or due to min len
#     - If mismatch is found, we break cuz any of the following characters don't mean anything,
#       as sorting is done based on the first mismatch
#     - If we exited cuz of min len and we find that w1 has greater len that means we have a case like
#       "apple" < "app" which is bad orering
# 3. Return true if false wasn't returned at every consecutive two word comparison

# Time: O(M * N) M words, N is average len of each word
# Space: O(1)