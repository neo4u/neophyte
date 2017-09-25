Dir['graphs/*.rb'].each do |file|
  require_relative File.join('../', File.dirname(file), File.basename(file, File.extname(file)))
end

require 'support/graphs_helpers'

describe '#bfs' do
  it 'Should return all nodes after traversing them' do
    graphs_enum = define_graphs()
    graphs_enum.each do |index_graph|
      index, graph = index_graph
      case index
      when 1
        expect(bfs(graph).to_a).to eql(%w[A B C D E F])
      when 2
        expect(bfs(graph).to_a).to eql(%w[A B C D E F])
      when 3
        expect(bfs(graph).to_a).to eql(%w[A B C D E F])
      end
    end
  end
end

describe '#bfs_recursive' do
  it 'Should return all nodes after traversing them recursively' do
    graphs_enum = define_graphs()
    graphs_enum.each do |index_graph|
      index, graph = index_graph
      case index
      when 1
        expect(bfs_recursive(graph).to_a).to eql(%w[A B C D E F])
      when 2
        expect(bfs_recursive(graph).to_a).to eql(%w[A B C D E F])
      when 3
        expect(bfs_recursive(graph).to_a).to eql(%w[A B C D E F])
      end
    end
  end
end
