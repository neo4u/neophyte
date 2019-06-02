# Approach 1: Store message and timestamp. We can do better by storing only the last 10 messages
class Logger_Hash
    def initialize()
        @hash = {}
    end

    def should_print_message(timestamp, message)
        digest = Digest::MD5.hexdigest(message)
        time_diff = timestamp - @hash[digest]
        if @hash.key?(digest) && time_diff >= 10
            @hash[digest] = timestamp
            true
        elsif @hash.key?(digest) && time_diff < 10
            false
        else
            @hash[digest] = timestamp
            true
        end
    end
end

class Logger
    def initialize()
        @msg_ts = {}
    end

    def should_print_message(ts, msg)
        if @msg_ts[msg] && ts - @msg_ts[msg] < 10
            false
        else
            @msg_ts[msg] = ts
            true
        end
    end
end

require 'digest'
require 'pqueue' # Needs to be installed
require 'set'

# Approach 2: priority queue (Can use any normal queue if timestamps are givein in sorted order as shown below)
# Needs pqueue gem installed
class Log
    attr_accessor :ts, :digest
    def initialize(ts, digest)
        @ts = ts
        @digest = digest
    end
end

class Logger_Q
    def initialize()
        @recent_logs_queue = PQueue.new(){ |a, b| a.ts < b.ts }
        @recent_messages = Set.new()
    end

    def should_print_message(timestamp, message)
        digest = Digest::MD5.hexdigest(message)
        while @recent_logs_queue.size() > 0
            log = @recent_logs_queue.top()
            # Discard the logs older than 10 secs
            if timestamp - log.ts >= 10
                @recent_logs_queue.pop()
                @recent_messages.delete(log.digest)
            else
                break
            end
        end

        result = !@recent_messages.include?(digest)
        if result
            @recent_logs_queue.push(Log.new(timestamp, digest))
            @recent_messages.add(digest)
        end

        result
    end
end

# Approach 3: Normal queue [B'cuz timestamps are given in increasing order]
require 'digest'
require 'set'

class Log
    attr_accessor :ts, :digest
    def initialize(ts, digest)
        @ts = ts
        @digest = digest
    end
end

class Logger
    def initialize()
        @logs_queue = []
        @last_10 = Set.new()
    end

    def should_print_message(timestamp, message)
        digest = Digest::MD5.hexdigest(message)
        while @logs_queue.size() > 0
            log = @logs_queue.first
            # Discard the logs older than 10 secs
            if timestamp - log.ts >= 10
                @logs_queue.shift()
                @last_10.delete(log.digest)
            else
                break
            end
        end

        result = !@last_10.include?(digest)
        if result
            @logs_queue.push(Log.new(timestamp, digest))
            @last_10.add(digest)
        end

        result
    end
end




# Approach 1: Hashmap
# 1. Use a hashmap to map message digest of message to recent print time
# 2. Each time a new print:
#       if digest in hash and time diff is >= 10, update timestamp and return true
#       else if digest in hash and time diff is < 10 then return false
#       else (digest not in hash), enter digest, timestamp into hash and return true
# Cons: But this way, we need store digests and thus has space complexity O(n)

# Approach 2 & 3: PriorityQueue/Heap or FIFO queue,
# Complexity: Time: worst case: O(n), n pops where n is the given timestamp and Space: O(1) as we only store 10 digests of fixed size
# 1. Use a min priorityqueue (lease timestamp on top) to save the digest and timestamp of message prints
# 2. each message print query we do the following:
#   - We check the timestamp difference between the incoming msg and top of queue
#   - We keep popping and deleting the digests from the set of last_10 messages
#   - We add the message digest to last_10 and return true if the digest in not present in last_10
#   - We return false if message is already present in last_10

# 359. Logger Rate Limiter
# https://leetcode.com/problems/logger-rate-limiter/description/


require 'test/unit'
extend Test::Unit::Assertions

l = Logger.new()
assert_equal(l.should_print_message(1,"foo"), true)
assert_equal(l.should_print_message(2,"bar"), true)
assert_equal(l.should_print_message(3,"foo"), false)
assert_equal(l.should_print_message(8,"bar"), false)
assert_equal(l.should_print_message(10,"foo"), false)
assert_equal(l.should_print_message(11,"foo"), true)

l = Logger.new()
assert_equal(l.should_print_message(1,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)
assert_equal(l.should_print_message(2,"bar"), true)
assert_equal(l.should_print_message(3,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(8,"bar"), false)
assert_equal(l.should_print_message(10,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(11,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)
assert_equal(l.should_print_message(15,"bar"), true)
assert_equal(l.should_print_message(20,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(21,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)
assert_equal(l.should_print_message(29,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(31,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)

l = Logger_Q.new()
assert_equal(l.should_print_message(1,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)
assert_equal(l.should_print_message(2,"bar"), true)
assert_equal(l.should_print_message(3,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(8,"bar"), false)
assert_equal(l.should_print_message(10,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(11,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)
assert_equal(l.should_print_message(15,"bar"), true)
assert_equal(l.should_print_message(20,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(21,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)
assert_equal(l.should_print_message(29,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), false)
assert_equal(l.should_print_message(31,"sairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairamsairam"), true)