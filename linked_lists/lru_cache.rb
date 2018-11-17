class Node
    def initialize(k, v)
        @key = k
        @val = v
        @prv, @nxt = nil, nil
    end
end

class LRUCache
    def initialize(capacity)
        @capacity = capacity
        @dict = {}
        @hea, @tail = Node.new(0, 0), Node.new(0, 0)

        @head.next, @tail.prev = @tail, @head
    end

    def get(key)
        return - 1 if !@dict.key?(key)

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
            n = @head.next
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