# # Best solution
# def valid_ip_address(ip)
#     if ip.match?(/\A\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\Z/)
#         ip_decimals = ip.split(".")
#         ip_decimals.each do |num|
#             return "Neither" if num.to_i > 255
#             return "Neither" if num.to_i == 0 && num.length > 1
#             return "Neither" if num.to_i != 0 && num[0] == '0'
#         end
#         return "IPv4"
#     elsif ip.match?(/\A([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\Z/)
#         return "IPv6"
#     end
#     return "Neither"
# end


# def valid_ip_address_regex(ip)
#     return "IPv4" if /^(25[0-5]|2[0-4][0-9]|[1][0-9]{2}|[1-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[1][0-9]{2}|[1-9][0-9]?|[0-9])\.(25[0-5]|2[0-4][0-9]|[1][0-9]{2}|[1-9][0-9]?|[0-9])\.(25[0-5]|2[0-4][0-9]|[1][0-9]{2}|[1-9][0-9]?|[0-9])$/ === ip
#     return "IPv6" if /^[a-fA-F0-9]{1,4}\:[a-fA-F0-9]{1,4}\:[a-fA-F0-9]{1,4}\:[a-fA-F0-9]{1,4}\:[a-fA-F0-9]{1,4}\:[a-fA-F0-9]{1,4}\:[a-fA-F0-9]{1,4}\:[a-fA-F0-9]{1,4}$/ === ip
#     return "Neither"
# end


def valid_ip_address_detailed(ip)
    tryIP4 = ip.split(".")
    return 'IPv4' if tryIP4.length == 4 && ip[0] != "." && ip[-1] != "." && validateIPv4(tryIP4)

    tryIP6 = ip.split(":")
    return 'IPv6' if tryIP6.length == 8 && ip[0] != ":" && ip[-1] != ":" && validateIPv6(tryIP6)

    "Neither"
end

def validateIPv4(groups)
    groups.each do |group|
        return false if group[0] == '0' && group != '0'
        return false if group.length < 1
        return false if group.to_i > 255
        digits = '1234567890'.chars
        group.each_char {|char| return false if !digits.include?(char)}
    end
    true
end

def validateIPv6(groups)
    groups.each do |group|
        return false if group.empty? || group.length > 4
        chars = "1234567890abcdefABCDEF".chars
        group.each_char {|char| return false if !chars.include?(char)}
    end
    true
end

# def validate_ip(ip)
#     parts = ip.split('.')
#     return false if parts.size != 4
#     return parts.map { |part| valid_part?(part) }.all?
# end

# def valid_part?(part)
#     ip = ''
#     part.each_char do |c|
#         ip += c if c.between?('0', '9')
#     end

#     ip.to_i.between?(0, 255)
# end




# 468. Validate IP Address
# https://leetcode.com/problems/validate-ip-address/description/


require 'test/unit'
extend Test::Unit::Assertions

# assert_equal(valid_ip_address("2001:0db8:85a3:0:0:8A2E:0370:7334:"), 'Neither')

assert_equal(validate_ip("127[.]0[.]0[.]1"), true)
assert_equal(validate_ip("127.0.0.1"), true)
assert_equal(validate_ip("127/./0[.]0[.]1"), true)
assert_equal(validate_ip("127asdfasdf[.]0[.]0[.]256"), false)
