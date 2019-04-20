#    This is Master's API interface.
#    You should not implement it, or speculate about its implementation
#
# class Master
# =begin
#     :type word: String
#     :rtype: Integer
# =end
#     def guess(word)
#         ...
#     end
# end
#

# Approach 1: Reduce wordlist to words that match with first guess
# @param {String[]} wordlist
# @param {Master} master
# @return {Void}
def find_secret_word(wordlist, master)
    n = 0
    while n < 6
        guess = wordlist.sample
        n = master.guess(guess)
        wordlist = wordlist.select { |w| match(w, guess) == n }
    end
end

def match(w1, w2)
    w1.chars.zip(w2.chars).map { |c1, c2| c1 == c2 ? 1 : 0 }.reduce(0, :+)
end

# Approach 2: MinMax
# @param {String[]} wordlist
# @param {Master} master
# @return {Void}
def find_secret_word(wordlist, master)
    n = 0
    while n < 6
        counts = Hash.new { |h, k| h[k] = 0 }
        wordlist.permutation(2).map { |w1, w2| w1 if match(w1, w2) == 0 }.each { |w| counts[w] += 1 }
        guess = wordlist.min_by { |w| counts[w] }
        n = master.guess(guess)
        wordlist = wordlist.select { |w| match(w, guess) == n }
    end
end


def match(w1, w2)
    w1.chars.zip(w2.chars).map { |c1, c2| c1 == c2 ? 1 : 0 }.reduce(0, :+)
end



# Approach 1: Reduce wordlist by eliminating using match size
# Steps:
# 1. Loop till match size == 6
# 2. Take a random choice from list and capture match size
# 3. Now only select words from wordlist that have similar
#    match size as they are candidates for secret.
# Time: O(n)
# Space: O(1)


# Approach 2: MinMax
# Steps:
# 1. Choose a word that has closest distance to the maximum number of words in wordlist
# 2. Use that as the first guess and get the distance from secret.
# 3. We get to eliminate all the words that don't have that distance,
#    because they can't be candidates as they don't have
#    the same distance from the first guess word as secret.
# 4. We continue the loop till we get a correct guess,
#    eliminating words and choosing the closest word,
# Time: O(n^2)
# Space: O(n^2)