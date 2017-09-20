class Vertex
  attr_accessor :id, :neighbors

  def initialize(id)
    @id = id
    @neighbors = []
  end
end

class Graph
  attr_accessor :vertices, :edges

  def initialize(adj_list = nil, adj_mat = nil, vertex_list = nil)
    @vertices = []
    raise "Vertex list and Adj_mat can't both be Empty." if vertex_list.nil? && adj_mat.nil?
    raise "Adj list and Adj_mat can't both be empty." if adj_list.nil? && adj_mat.nil?
    raise "Don't use both adjacency matrix and list." if !adj_list.nil? && !adj_mat.nil?
    set_vertices(vertex_list)
    adj_mat.nil? && !adj_list.nil? ? set_edges_from_list(adj_list) : set_edges_from_matrix(adj_mat)
  end

  def set_vertices(list)
    list.each do |id|
      vertices[id] = Vertex.new(id)
    end
  end

  def find_path(v1, v2, path = [])
    path += [v1]
    return path if v1.eql?(v2)
    return nil unless vertices.include?(v1)

    @vertices.each do |v|
      unless path.include?(v)
        new_path = find_path(node, v2, path)
        return newpath unless new_path.nil?
      end
    end

    nil
  end

  def visit(city)
    visited[city.id] = true
    city.neighbors.reject(&:nil?).each do |neighbor|
      unless visited[neighbor.id]
        @total_cost += road_cost
        visit(neighbor)
      end
    end
  end

  def set_edges_from_list(adj_list)
    adj_list.each do |v, neighbour_list|
      add_edges(v, neighbour_list)
    end
  end

  def add_edges(v, neighbour_list)
    vertices[v].neighbors += neighbour_list
  end
end

adj_list = {
  A: ['B', 'C'],
  B: ['C', 'D'],
  C: ['D'],
  D: ['C'],
  E: ['F'],
  F: ['C']
}

graph = Graph.new(adj_list)
graph.find_path('A', 'D')
