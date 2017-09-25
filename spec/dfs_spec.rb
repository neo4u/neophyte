Dir['graphs/*.rb'].each do |file|
  require_relative File.join('../', File.dirname(file), File.basename(file, File.extname(file)))
end

require 'support/graphs_helpers'

describe '#dfs' do
  it 'Should return all nodes after traversing them' do
    graphs_enum = define_graphs()
    graphs_enum.each do |index_graph|
      index, graph = index_graph
      case index
      when 1
        expect(dfs(graph).to_a).to eql(%w[A C F E B D])
      when 2
        expect(dfs(graph).to_a).to eql(%w[A B C D E F])
      when 3
        expect(dfs(graph).to_a).to eql(%w[A B C D E F])
      end
    end
  end
end

describe '#dfs_recursive' do
  it 'Should return all nodes after traversing them recursively' do
    graphs_enum = define_graphs()
    graphs_enum.each do |index_graph|
      index, graph = index_graph
      case index
      when 1
        expect(dfs_recursive(graph).to_a).to eql(%w[A B D E F C])
      when 2
        expect(dfs_recursive(graph).to_a).to eql(%w[A B C E D F])
      when 3
        expect(dfs_recursive(graph).to_a).to eql(%w[A B C D E F])
      end
    end
  end
end

describe '#dfs_paths' do
  it 'Should return a path from src to dst' do
    graphs_enum = define_graphs()
    graphs_enum.each do |index_graph|
      index, graph = index_graph
      case index
      when 1
        expect(dfs_paths(graph, 'A', 'F')).to eql([[%w[A C F], %w[A B E F]], %w[A C F]])
        expect(dfs_paths(graph, 'A', 'C')).to eql([[%w[A C], %w[A B E F C]], %w[A C]])
        expect(dfs_paths(graph, 'A', 'G')).to eql([[], nil])
      end
    end
  end
end

describe '#dfs_paths_recursive' do
  it 'Should return a path from src to dst, recursively' do
    graphs_enum = define_graphs()
    graphs_enum.each do |index_graph|
      index, graph = index_graph
      case index
      when 1
        expect(dfs_paths(graph, 'A', 'F')).to eql([%w[A B E F], [%w[A C F]], %w[A C F]])
        expect(dfs_paths(graph, 'A', 'C')).to eql([[%w[A B E F C], %w[A C]], %w[A C]])
        expect(dfs_paths(graph, 'A', 'G')).to eql([[], nil])
      end
    end
  end
end

describe '#connected_components' do
  it 'Should return a list of connected components' do
    graphs_enum = define_graphs()
    graphs_enum.each do |index_graph|
      index, graph = index_graph
      case index
      when 4
        expect(connected_components(graph)).to eql([%w[A B C D E F], %w[G]])
      when 5
        expect(connected_components(graph)).to eql([%w[A B C D E F], %w[G H I J]])
      end
    end
  end
end