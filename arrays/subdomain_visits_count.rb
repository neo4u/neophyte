# @param {String[]} cpdomains
# @return {String[]}
def subdomain_visits(cpdomains)
    map = Hash.new(0)
    cpdomains.each do |dom|
        cnt, d = dom.split
        cnt, sub_ds = cnt.to_i, d.split('.')
        0.upto(sub_ds.size - 1) do |i|
            sd = sub_ds[i..-1].join('.')
            map[sd] += cnt
        end
    end

    map.map { |k, v| "#{v} #{k}" }
end


# 811. Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(subdomain_visits(["9001 discuss.leetcode.com"]).sort, ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"].sort)
assert_equal(subdomain_visits(["9001 discuss.leetcode.com", '1 yahoo.com']).sort, ["9001 leetcode.com","9001 discuss.leetcode.com","9002 com"].sort)