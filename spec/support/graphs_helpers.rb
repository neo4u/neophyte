module Helpers
  def define_graphs
    graph1 = {
      'A' => Set.new(['B', 'C']),
      'B' => Set.new(['A', 'D', 'E']),
      'C' => Set.new(['A', 'F']),
      'D' => Set.new(['B']),
      'E' => Set.new(['B', 'F']),
      'F' => Set.new(['C', 'E'])
    }

    graph2 = {
      'A' => Set.new(['B']),
      'B' => Set.new(['A', 'C']),
      'C' => Set.new(['B', 'E', 'D']),
      'D' => Set.new(['C', 'E']),
      'E' => Set.new(['B', 'C', 'D', 'F']),
      'F' => Set.new(['E'])
    }

    graph3 = {
      'A' => Set.new(['B']),
      'B' => Set.new(['A', 'C']),
      'C' => Set.new(['B', 'D']),
      'D' => Set.new(['C', 'E']),
      'E' => Set.new(['D', 'F']),
      'F' => Set.new(['E'])
    }

    graph4 = {
      'A' => Set.new(['B', 'C']),
      'B' => Set.new(['A', 'D', 'E']),
      'C' => Set.new(['A', 'F']),
      'D' => Set.new(['B']),
      'E' => Set.new(['B', 'F']),
      'F' => Set.new(['C', 'E']),
      'G' => Set.new([])
    }

    graph5 = {
      'A' => Set.new(['B', 'C']),
      'B' => Set.new(['A', 'D', 'E']),
      'C' => Set.new(['A', 'F']),
      'D' => Set.new(['B']),
      'E' => Set.new(['B', 'F']),
      'F' => Set.new(['C', 'E']),
      'G' => Set.new(['H', 'I']),
      'H' => Set.new(['J', 'G']),
      'I' => Set.new(['G', 'J']),
      'J' => Set.new(['H', 'I'])
    }

    graphs = [graph1, graph2, graph3, graph4, graph5]
    enumerator = Enumerator.new do |y|
      y.yield(graphs.shift) until graphs.empty?
    end
    enumerator
  end
end

RSpec.configure do |c|
  c.include Helpers
end