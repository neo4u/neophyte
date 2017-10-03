Dir['sorting/*.rb'].each do |file|
  require_relative File.join('../', File.dirname(file), File.basename(file, File.extname(file)))
end

describe '#merge_sort' do
  it 'Should sort arrays' do
    expect(merge_sort([5, 6, 7, 8, 1, 2, 3, 4])).to eql([1, 2, 3, 4, 5, 6, 7, 8])
  end

  it 'Should sort arrays' do
    expect(merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).to eql([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
  end

  it 'Should sort arrays' do
    expect(merge_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5])).to eql([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
  end
end

describe '#counting_sort' do
  it 'Should sort arrays' do
    expect(counting_sort([5, 6, 7, 8, 1, 2, 3, 4])).to eql([1, 2, 3, 4, 5, 6, 7, 8])
  end

  it 'Should sort arrays' do
    expect(counting_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).to eql([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
  end

  it 'Should sort arrays' do
    expect(counting_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5])).to eql([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
  end
end

describe '#heap_sort' do
  it 'Should sort arrays' do
    expect(heap_sort([5, 6, 7, 8, 1, 2, 3, 4])).to eql([1, 2, 3, 4, 5, 6, 7, 8])
  end

  it 'Should sort arrays' do
    expect(heap_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5])).to eql([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
  end

  it 'Should sort arrays' do
    expect(heap_sort([0, 1, 2, 3, 4, 5, 6, 7, -10, 9, 0, 11])).to eql([-10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11])
  end

  it 'Should sort arrays' do
    expect(heap_sort([0, 1, 2, 3, 4, -50000, 6, 7, 8, 9, 10, 11])).to eql([-50000, 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11])
  end
end