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

    graph6 = {
      's' => { 'a' => 2, 'b' => 1 },
      'a' => { 's' => 3, 'b' => 4, 'c' => 8 },
      'b' => { 's' => 4, 'a' => 2, 'd' => 2 },
      'c' => { 'a' => 2, 'd' => 7, 't' => 4 },
      'd' => { 'b' => 1, 'c' => 11, 't' => 5 },
      't' => { 'c' => 3, 'd' => 5 }
    }
    graph8 = {
      'a' => { 'b' => -1, 'c' =>	4 },
      'b' => { 'c' =>	3, 'd' =>	2, 'e' => 2 },
      'c' => {},
      'd' => { 'b' =>	1, 'c' => 5 },
      'e' => { 'd' => -3 }
    }

    graphs = [graph1, graph2, graph3, graph4, graph5, graph6, nil, graph8]
    enumerator = Enumerator.new do |y|
      y.yield(graphs.shift) until graphs.empty?
    end
    enumerator
  end
end

RSpec.configure do |c|
  c.include Helpers
end