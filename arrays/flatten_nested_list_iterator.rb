# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
#
#class NestedInteger
#    def is_integer()
#        """
#        Return true if this NestedInteger holds a single integer, rather than a nested list.
#        @return {Boolean}
#        """
#
#    def get_integer()
#        """
#        Return the single integer that this NestedInteger holds, if it holds a single integer
#        Return nil if this NestedInteger holds a nested list
#        @return {Integer}
#        """
#
#    def get_list()
#        """
#        Return the nested list that this NestedInteger holds, if it holds a nested list
#        Return nil if this NestedInteger holds a single integer
#        @return {NestedInteger[]}
#        """

class NestedIterator
    # @param {NestedInteger[]} nested_list
    def initialize(nested_list)
        @stack = []
        nested_list.reverse_each { |item| @stack.push(item) }
    end

    # @return {Boolean}
    def has_next
        while !@stack.empty?
            curr = @stack.last
            return true if curr.is_integer()
            @stack.pop()
            curr.get_list.reverse_each { |item| @stack.push(item) }
        end

        false
    end

    # @return {Integer}
    def next
        @stack.pop.get_integer()
    end
end

# Your NestedIterator will be called like this:
# i, v = NestedIterator.new(nested_list), []
# while i.has_next()
#    v << i.next
# end


# 341. Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/