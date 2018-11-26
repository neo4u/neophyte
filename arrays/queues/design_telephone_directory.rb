require 'set'

class PhoneDirectory

    def initialize(max_numbers)
        @available = Set.new((0...max_numbers).to_a)
    end

    def get()
        first = @available.empty? ? -1 : @available.first
        @available.delete(first) if first != -1

        first
    end

    def check(number)
        @available.include?(number)
    end

    def release(number)
        @available.add(number)
    end
end

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory.new(max_numbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

# 379. Design Phone Directory
# https://leetcode.com/problems/design-phone-directory/
