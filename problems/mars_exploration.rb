#!/bin/ruby
# --------------------------------------------------------------------------------
# Letters in some of the SOS messages are altered by cosmic radiation during transmission.
# Given the signal received by Earth as a string, S, determine how many letters of Sami's SOS have been changed by radiation.
# Input Format
# There is one line of input: a single string, S.
# Note: As the original message is just SOS repeated n times, S's length will be a multiple of 3.
# Output Format: Print the number of letters in Sami's message that were altered by cosmic radiation.
# Sample Input 0: SOSSPSSQSSOR
# Sample Output 0: 3
# Sample Input 1: SOSSOT
# Sample Output 1: 1
# --------------------------------------------------------------------------------

def sig_changes(s)
  mods = 0
  s.chars.each_slice(3) do |c1, c2, c3|
    mods += if c1.eql?('S') && c2.eql?('O') && c3.eql?('S')
              0
            elsif (c1.eql?('S') && !c2.eql?('O') && !c3.eql?('S')) ||
                  ( !c1.eql?('S') && c2.eql?('O') && !c3.eql?('S') ) ||
                  ( !c1.eql?('S') && !c2.eql?('O') && c3.eql?('S') )
              2
            elsif ( !c1.eql?('S') && c2.eql?('O') && c3.eql?('S') ) ||
                  ( c1.eql?('S') && !c2.eql?('O') && c3.eql?('S') ) ||
                  ( c1.eql?('S') && c2.eql?('O') && !c3.eql?('S') )
              1
            else
              3
            end
  end

  mods
end

s = gets.strip
puts sig_changes(s)
