require 'set'

N, I = gets.split.map(&:to_i)
list_of_sets = []

I.times do
  a, b = gets.split.map(&:to_i)
  new_set = Set.new []
  set_len = list_of_sets.length
  s = 0
  while s < set_len
    if list_of_sets[s].include?(a) || list_of_sets[s].include?(b)
      new_set |= list_of_sets[s]
      list_of_sets.delete_at(s)
      set_len -= 1
    else
      s += 1
    end
  end
  new_set |= [a, b]
  list_of_sets << new_set
end

answer = N * (N - 1) / 2
list_of_sets.each { |set| answer -= set.length * (set.length - 1) / 2 }

puts answer

# def dfs(cur)
#   return 0 if @color[cur] != 0
#   @color[cur] = 1
#   count = 1
#   (@adj_list[cur] || []).each do |ch|
#     count += dfs(ch)
#   end
#   count
# end