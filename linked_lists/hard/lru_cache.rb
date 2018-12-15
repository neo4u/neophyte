class Node
    attr_accessor :key, :val, :prv, :nxt

    def initialize(k, v)
        @key = k
        @val = v
        @prv, @nxt = nil, nil
    end
end

class LRUCache
    attr_accessor :head, :tail, :dict, :capacity
    def initialize(capacity)
        @capacity = capacity
        @dict = Set.new()
        @head, @tail = Node.new(0, 0), Node.new(0, 0)

        @head.nxt, @tail.prv = @tail, @head
    end

    def get(key)
        return -1 if !@dict.key?(key)

        n = @dict[key]
        remove(n)
        add(n)

        n.val
    end

    def put(key, value)
        remove(@dict[key]) if @dict.key?(key)
        
        n = Node.new(key, value)
        add(n)
        @dict[key] = n

        if @dict.size > @capacity
            n = @head.nxt
            remove(n)
            @dict.delete(n.key)
        end
    end

    private
    def remove(node)
        p = node.prv
        n = node.nxt
        p.nxt = n
        n.prv = p
    end

    def add(node)
        p = tail.prv
        p.nxt = node
        @tail.prv = node
        node.prv = p
        node.nxt = @tail
    end
end


# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/

require 'test/unit'
extend Test::Unit::Assertions

cache = LRUCache.new(2)

cache.put(1, 1)
cache.put(2, 2)
assert_equal(cache.get(1), 1)
cache.put(3, 3)
assert_equal(cache.get(2), -1)
cache.put(4, 4)
assert_equal(cache.get(1), -1)
assert_equal(cache.get(3), 3)
assert_equal(cache.get(4), 4)

