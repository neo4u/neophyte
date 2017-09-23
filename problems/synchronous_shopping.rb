# frozen_string_literal: true
require 'set'
require 'ruby-prof'
require 'byebug'
# $f = File.open ARGV[0]

def read_nums
  # $f.gets.strip.split.map(&:to_i)
  gets.strip.split.map(&:to_i)
end

# --------------------------------------------------------------------------------
# 
# --------------------------------------------------------------------------------
class Town
  attr_reader :mincost

  def initialize
    max_shop = 1000 + 1
    max_fish = 1 << 10
    @shops = Array.new(max_shop, 0)
    @road = Array.new(max_shop) { [] }
    @distance = Array.new(max_shop) { Array.new(max_fish) { Float::INFINITY } }
    init
    dijk
    min_cost
  end

  def init
    @total_shops, total_roads, @total_fish = read_nums
    add_fish2shop
    get_road(total_roads)
    @mincost = Float::INFINITY
    init_travel
  end

  def add_fish2shop
    i = 1
    loop do
      total, *types = read_nums
      @shops[i] = bits(types)
      i += 1
      break if i > @total_shops
    end
  end

  def bits(types)
    types.reduce(0) { |bor, type| bor | 1 << (type - 1) }
  end

  def get_road(total_roads)
    (1..total_roads).each do
      shop_x, shop_y, distance = read_nums
      @road[shop_x].push([shop_y, distance])
      @road[shop_y].push([shop_x, distance])
    end
  end

  def init_travel
    @distance[1][@shops[1]] = 0
    @queue = Set.new [
      [
        1, @shops[1], @distance[1][@shops[1]]
      ]
    ]
  end

  def min_cost
    all_types = (1 << @total_fish) - 1
    (0..all_types).each do |little_cat_collected|
      (0..all_types).each do |big_cat_collected|
        next if big_cat_collected | little_cat_collected != all_types
        cost = [@distance[@total_shops][little_cat_collected], @distance[@total_shops][big_cat_collected]].max
        @mincost = [@mincost, cost].min
      end
    end
  end

  def dijk
    until @queue.empty?
      last_travel = @queue.first
      @queue.delete last_travel
      dijk_neighbour(last_travel)
    end
  end

  # last_travel: shop_number, fish_collected, distance_to_this_shop
  def dijk_neighbour(last_shop, last_collected, distance_to_last_shop)
    # last_shop, last_collected, distance_to_last_shop = last_travel
    @road[last_shop].each do |current_shop|
      current_shop_number, distance_from_last_shop = current_shop
      collected = last_collected | @shops[current_shop_number]
      distance_to_current_shop = distance_to_last_shop + distance_from_last_shop
      dijk_queue(current_shop_number, distance_to_current_shop, collected)
    end
  end

  def dijk_queue(current_shop_number, distance_to_current_shop, collected)
    travelled_distance = @distance[current_shop_number][collected]
    return if distance_to_current_shop >= travelled_distance

    @queue.delete [current_shop_number, collected, travelled_distance]
    @distance[current_shop_number][collected] = distance_to_current_shop
    @queue << [current_shop_number, collected, @distance[current_shop_number][collected]]
  end
end

# RubyProf.start
t = Town.new
puts t.mincost
# result = RubyProf.stop
# RubyProf::GraphPrinter.new(result).print(STDOUT, {})
