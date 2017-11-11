require 'support/graphs_helpers'
require_relative "../graphs/dfs_practice"

describe 'dfs.rb' do
  before(:all) { @graphs = define_graphs().to_a }

  describe '#dfs_iterative' do
    it 'Should return all nodes after traversing them' do
      expect(dfs_iterative(@graphs[0], 'A').to_a).to eql(%w[A C F E B D])
    end

    it 'Should return all nodes after traversing them' do
      expect(dfs_iterative(@graphs[1], 'A').to_a).to eql(%w[A B C D E F])
    end

    it 'Should return all nodes after traversing them' do
      expect(dfs_iterative(@graphs[2], 'A').to_a).to eql(%w[A B C D E F])
    end
  end

  describe '#dfs' do
    it 'Should return all nodes after traversing them recursively' do
      expect(dfs(@graphs[0], 'A').to_a).to eql(%w[A B D E F C])
    end

    it 'Should return all nodes after traversing them recursively' do
      expect(dfs(@graphs[1], 'A').to_a).to eql(%w[A B C E D F])
    end

    it 'Should return all nodes after traversing them recursively' do
      expect(dfs(@graphs[2], 'A').to_a).to eql(%w[A B C D E F])
    end
  end

  describe '#dfs_paths_iterative' do
    it 'Should return a path from src to dst' do
      expect(dfs_paths_iterative(@graphs[0], 'A', 'F')).to eql([[%w[A C F], %w[A B E F]], %w[A C F]])
      expect(dfs_paths_iterative(@graphs[0], 'A', 'C')).to eql([[%w[A C], %w[A B E F C]], %w[A C]])
      expect(dfs_paths_iterative(@graphs[0], 'A', 'G')).to eql([[], nil])
    end
  end

  describe '#dfs_path' do
    it 'Should return a path from src to dst, recursively' do
      expect(dfs_paths(@graphs[0], 'A', 'F')).to eql([[%w[A B E F], %w[A C F]], %w[A C F]])
      expect(dfs_paths(@graphs[0], 'A', 'C')).to eql([[%w[A B E F C], %w[A C]], %w[A C]])
      expect(dfs_paths(@graphs[0], 'A', 'G')).to eql([[], nil])
    end
  end

  describe '#connected_components' do
    it 'Should return a list of connected components' do
      expect(connected_components(@graphs[3])).to eql([%w[A B C D E F], %w[G]])
    end

    it 'Should return a list of connected components' do
      expect(connected_components(@graphs[4])).to eql([%w[A B C D E F], %w[G H I J]])
    end
  end

  # describe '#dijkstra' do
  #   it 'Should return a list of shortest paths and the shortest distance' do
  #     graphs_enum = define_graphs()
  #     graphs_enum.each do |index_graph|
  #       index, graph = index_graph
  #       case index
  #       when 6
  #         expect(dijkstra(graph, 's', 't')).to eql([['t', 'd', 'b', 's'], 8])
  #       end
  #     end
  #   end
  # end

  describe '#bellman_ford' do
    it 'Should return a list of shortest paths and the shortest distance' do
      d = { 'a' => 0, 'b' => -1, 'c' => 2, 'd' => -2, 'e' => 1 }
      p = { 'a' => nil, 'b' => 'a', 'c' => 'b', 'd' => 'e', 'e' => 'b' }
      expect(bellman_ford(@graphs[7], 'a')).to eql([d, p])
    end
  end
end
