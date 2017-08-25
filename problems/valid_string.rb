#!/usr/bin/env ruby

# ------------------------------------------------------------------------------------------
# Sherlock and the Valid String
# ------------------------------------------------------------------------------------------
# VALID => if counts_of_counts.size.eql?(1) # This condition means that all chars had same counts
# ------------------------------------------------------------------------------------------
# VALID => if counts_of_counts.size.eql?(2) && counts_of_counts.include?(1) && counts_of_counts[1] < 2
# 1. This means there were two different counts and
# 2. at least one of the chars' counts was 1 and
# 3. the number of chars that appeared only once is less than 2
# which means one deletion is sufficient to make all chars have same repititions
# ------------------------------------------------------------------------------------------
# VALID => if counts_of_counts.size.eql?(2) && !counts_of_counts.include?(1) && (counts_of_counts.keys[0] - counts_of_counts.keys[1]).abs.eql?(1)
# 1. This means there were two different counts and
# 2. One of them isn't a single char appearance and
# 3. The char that doesn't have equal count as the rest of the chars has only 1 repitition more
# Thus one deletion should give us the string with all chars with same counts
# -----------------------------------------------------------------------------------------
# INVALID => If there is more than 2 counts it means we need more than one deletion and hence not valid
# ------------------------------------------------------------------------------------------
def valid?(s)
  counts = {}                                       # Build a hash of counts for each char
  s.chars.each do |c|                               # Loop to capture counts
    counts[c].nil? ? counts[c] = 1 : counts[c] += 1 # ternary op to return 1 or increment by 1
  end
  # All chars that have the same number of repetitions
  # will be clubbed into one entry in this hash
  counts_of_counts = {}                             # Build a hash of counts of counts
  counts.values.each do |v|                         # Loop through the values and sort in to a hash
    counts_of_counts[v].nil? ? counts_of_counts[v] = 1 : counts_of_counts[v] += 1
  end

  valid = if counts_of_counts.size.eql?(1)
            'YES'
          elsif counts_of_counts.size.eql?(2) && counts_of_counts.include?(1) && counts_of_counts[1] < 2
            'YES'
          elsif counts_of_counts.size.eql?(2) && !counts_of_counts.include?(1) && (counts_of_counts.keys[0] - counts_of_counts.keys[1]).abs.eql?(1)
            'YES'
          else
            'NO'
          end
  valid
end

s = gets.strip
result = valid?(s)
puts result
