# @param {String} secret
# @param {String} guess
# @return {String}
def get_hint(secret, guess)
    bulls, cows, n = 0, 0, secret.size
    nums = Array.new(10, 0)

    0.upto(n - 1) do |i|
        s, g = secret[i].to_i, guess[i].to_i

        if s == g
            bulls += 1
        else
            cows += 1 if nums[s] < 0  # we've seen s before in guess string
            cows += 1 if nums[g] > 0  # we've seen g before in secret string
            nums[s] += 1
            nums[g] -= 1
        end
    end

    "#{bulls}A#{cows}B"
end

# 299. Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/description/

# Example 1: secret = '1807', guess = '7810'
# 1, 7: inc nums[1] and dec nums[7]
# s: 1 | g: 7 | bulls: 0 | cows: 0 | nums: [0, 1, 0, 0, 0, 0, 0, -1, 0, 0]
# 8, 8: bull
# s: 8 | g: 8 | bulls: 1 | cows: 0 | nums: [0, 1, 0, 0, 0, 0, 0, -1, 0, 0]
# 0, 1: inc nums[0] and dec nums[1], nums[g]: 1 > 0 so inc cows
# s: 0 | g: 1 | bulls: 1 | cows: 1 | nums: [1, 0, 0, 0, 0, 0, 0, -1, 0, 0]
# 7, 0: inc nums[7] and dec nums[0], nums[s]: -1 < 0, nums[g]: 1 > 0, inc + 2 cows
# s: 7 | g: 0 | bulls: 1 | cows: 3 | nums: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Example 2: secret = '1123', guess = '0111'
# s: 1 | g: 0 | bulls: 0 | cows: 0 | nums: [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# s: 1 | g: 1 | bulls: 1 | cows: 0 | nums: [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# s: 2 | g: 1 | bulls: 1 | cows: 1 | nums: [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# s: 3 | g: 1 | bulls: 1 | cows: 1 | nums: [-1, -1, 1, 1, 0, 0, 0, 0, 0, 0]

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(get_hint('1807', '7810'), '1A3B')
assert_equal(get_hint('1123', '0111'), '1A1B')
assert_equal(get_hint('1462', '1246'), '1A3B')
