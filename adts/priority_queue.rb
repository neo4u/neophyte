# ------------------------------------------------------------------------
# Binary Heap as per CLRS  THis should be changed to priority queue
# as PQ is the ADT and heap is the data structure
# ------------------------------------------------------------------------
class PriorityQueue
	attr_accessor :data

	def initialize(a)
		@size = a.size
		@data = build_max_heap(a)
	end

	def insert(x)
		alias :add :insert

		@data << x
		i = @size
		sift_up(@data, i)
		@size += 1

		@data
	end

	def delete(i)
		alias :remove :delete

		@data[i] = -Float::INFINITY
		@data[i], @data[-1] = @data[-1], @data[i]
		max_heapify(@data, i, @size)
		@size -= 1

		@data.pop
	end

	def increase_key(i, key)
		@data[i] = key
		sift_up(@data, i)

		@data
	end

	def peek
		alias :max :peek
		@data.first
	end

	def extract_max
		ret = @data[0]

		@data[0] = -Float::INFINITY
		@data[0], @data[-1] = @data[-1], @data[0]
		@data.pop
		@size -= 1
		max_heapify(@data, 0, @size)

		ret
	end

	def show
		puts "Data: #{@data}"
	end

	private
	def build_max_heap(a)
		(a.size/2 - 1).downto(0) do |i|
			max_heapify(a, i, a.size)
		end

		a
	end

	def max_heapify(a, i, heapsize)
		l = left_child(i)
		r = right_child(i)

		largest = 	if l < heapsize && a[l] > a[i]
						l
					else
						i
					end

		largest = r if r < heapsize && a[r] > a[largest]
		return if largest == i
		a[i], a[largest] = a[largest], a[i]

		max_heapify(a, largest, heapsize)
	end

	def left_child(i)
		2 * i + 1
	end

	def right_child(i)
		2 * i + 2
	end

	def parent(i)
		(i - 1) / 2
	end

	def sift_up(a, i)
		while a[parent(i)] < a[i] && parent(i) >= 0
			a[parent(i)], a[i] = a[i], a[parent(i)]
			i = parent(i)
		end
	end
end

require 'test/unit'
extend Test::Unit::Assertions

a = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
excepted_result = [11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2]
q = PriorityQueue.new(a)
assert_equal(excepted_result, q.data)
assert_equal([25, 9, 11, 7, 6, 10, 8, 3, 1, 4, 0, 2, 5], q.insert(25))
assert_equal(-Float::INFINITY, q.delete(0))
assert_equal([11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2], q.data)
assert_equal(-Float::INFINITY, q.remove(0))
assert_equal([10, 9, 8, 7, 6, 5, 2, 3, 1, 4, 0], q.data)
assert_equal(10, q.peek)
assert_equal(10, q.extract_max)
assert_equal([9, 7, 8, 3, 6, 5, 2, 0, 1, 4], q.data)
assert_equal([35, 7, 9, 3, 6, 5, 8, 0, 1, 4], q.increase_key(6, 35))
