class Node
    attr_accessor :prv, :nxt, :key, :val
    def initialize(k, v)
        @key, @val = k, v
        @prv, @nxt = nil, nil
    end
end


class LRUCache
    attr_accessor :head, :tail, :capacity, :dict
    def initialize(capacity)
        @capacity = capacity
        @head, @tail, @dict = Node.new(-Float::INFINITY, nil), Node.new(Float::INFINITY, nil), {}
        @head.nxt, @tail.prv = @tail, @head
    end

    def put(k, v)
        remove(@dict[k]) if @dict.key?(k)
        node = Node.new(k, v)
        add(node)
        @dict[k] = node
        if @dict.size > capacity
            node = @head.nxt
            remove(node)
            @dict.delete(node.key)
        end
    end

    def get(k)
        return -1 if !@dict.key?(k)

        node = @dict[k]
        remove(node)
        add(node)

        node.val
    end

    private
    def add(node)
        p = @tail.prv
        p.nxt, @tail.prv = node, node
        node.nxt, node.prv = @tail, p
    end

    def remove(node)
        return if !@dict.key?(node.key)
        p, n = node.prv, node.nxt
        p.nxt, n.prv = n, p
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

