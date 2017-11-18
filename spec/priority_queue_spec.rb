# a = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
# excepted_result = [11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2]
# q = PriorityQueue.new(a)
# assert_equal(excepted_result, q.data)
# assert_equal([25, 9, 11, 7, 6, 10, 8, 3, 1, 4, 0, 2, 5], q.insert(25))
# assert_equal(-Float::INFINITY, q.delete(0))
# assert_equal([11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2], q.data)
# assert_equal(-Float::INFINITY, q.remove(0))
# assert_equal([10, 9, 8, 7, 6, 5, 2, 3, 1, 4, 0], q.data)
# assert_equal(10, q.peek)
# assert_equal(10, q.extract_max)
# assert_equal([9, 7, 8, 3, 6, 5, 2, 0, 1, 4], q.data)
# assert_equal([35, 7, 9, 3, 6, 5, 8, 0, 1, 4], q.increase_key(6, 35))
# end

require_relative '../adts/priority_queue'

def init_q()
  a = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
  @q = PriorityQueue.new(a)
end

describe PriorityQueue do
  before(:all) { init_q() }

  describe '.insert' do
    it 'Heap should look as expected' do
      expect(@q.data).to       eql([11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2])
      expect(@q.insert(25)).to eql([25, 9, 11, 7, 6, 10, 8, 3, 1, 4, 0, 2, 5])
    end
  end

  describe '.delete' do
    it 'Should delete/remove stuff sensibly' do
      expect(@q.delete(0)).to eql(-Float::INFINITY)
      expect(@q.data).to      eql([11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2])
      expect(@q.remove(0)).to eql(-Float::INFINITY)
      expect(@q.data).to      eql([10, 9, 8, 7, 6, 5, 2, 3, 1, 4, 0])
    end
  end

  describe '.extract_max' do
    it 'Should extract_max the biggest element and should also peek the biggest element' do
      expect(@q.peek).to        eql(10)
      expect(@q.extract_max).to eql(10)
      expect(@q.data).to        eql([9, 7, 8, 3, 6, 5, 2, 0, 1, 4])
    end
  end

  describe '.increase_key' do
    it 'Should increase_key a element at position i to given key' do
      expect(@q.increase_key(6, 35)).to eql([35, 7, 9, 3, 6, 5, 8, 0, 1, 4])
    end
  end
end
