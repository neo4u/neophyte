# @param {Character[]} tasks
# @param {Integer} n
# @return {Integer}
def least_interval_alt(tasks, n)
  return tasks.length if n.zero?
  map = Hash.new(0)

  tasks.each do |task|
    map[task] += 1
  end

  queue, cooldown, current = [], {}, 0
  queue += map.values.sort.reverse

  while !queue.empty? || !cooldown.empty?
    if cooldown.key?(current - n - 1)
      task = cooldown.delete(current - n - 1)
      i = 0
      i += 1 while i < queue.size && queue[i] > task
      queue.insert(i, task)
    end

    unless queue.empty?
      left = queue.shift - 1
      cooldown[current] = left unless left.zero?
    end

    current += 1
  end

  current
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(least_interval_alt(["A","A","A","B","B","B"], 2), 8)
