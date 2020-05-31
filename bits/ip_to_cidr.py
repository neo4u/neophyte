from typing import List


class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        dec_ip, result = self.ip_to_dec(ip), []

        while n > 0:
            dec_t0s = self.trailing_0s_pow_2(dec_ip)
            ip = self.dec_to_ip(dec_ip)

            while dec_t0s > n: dec_t0s >>= 1 # same as div //= 2
            t0s = self.trailing_0s(dec_t0s)
            result.append(f"{ip}/{32 - t0s}")
            n -= dec_t0s
            dec_ip += dec_t0s
        return result

    def ip_to_dec(self, ip):
        a, b, c, d = list(map(int, ip.split('.')))
        return a * 256**3 + b * 256**2 + c * 256**1 + d * 256**0

    def dec_to_ip(self, dec):
        a, b, c, d = dec // 256**3 % 256, dec // 256**2 % 256, dec // 256**1 % 256, dec // 256**0 % 256
        return ".".join(map(str, [a, b, c, d]))

    def trailing_0s_pow_2(self, dec):
        # Find number of trailing zeros power 2 (dec_t0s
        return dec & -dec

    def trailing_0s(self, dec):
        count = 0

        while dec & 1 == 0:
            dec >>= 1
            count += 1

        return count


# 751. IP to CIDR
# https://leetcode.com/problems/ip-to-cidr/description/
# Copy this entire text in file and run with python3 and it should run perfectly

# Intuition:
# - A Subnet mask is a 32-bit number that masks an IP address,
#   and divides the IP address into network address and host address.
#   Subnet Mask is made by setting network bits to all "1"s and setting host bits to all "0"s.
# - CIDR notation is used to represent a block of IPs,
#   Ex: 192.168.100.0/22 represents 1024 address from 192.168.100.0 to 192.168.103.255.
# - In this question, given a starting IP, we need to find CIDR blocks such that they cover n IPs
# - If you know how to convert a decimal to binary and back, or decimal to hex and back, this approach is similar to that

# Steps:
# 1. We first convert the IP which can be seen as a base 256 number of 4 digits to it's deciaml value
# 2. Find number of trailing zeros power 2 (dec_t0s)
#    Trailing 0s give us the number of bits we are working with to define a mask
# 3. We reduce 'dec_t0s' by 2 while dec_t0s > n, ensurin we get the largest value without crossing n
#    THIS STEP IS KEY TO CHOOSING OPTIMAL CIDR BLOCKS to just cover n
#    Adding 2 ^ no. of trailing 0s to the decimal value of the IP will fill the trailing 0s with 1s
# 4. Parallely we can also get the IP from the decimal value of the IP we currently have,
#    (Note that this increase by 'dec_t0s' each iteration of while n > 0)
# 5. We then add the CIDR block representing the curr 'dec_t0s' size CIDR block
# 6. Then we add 'dec_t0s' to 'number' to fill the 0s, and also subtract dec_t0s from n,
#    cuz we've represented another dec_t0s IPs using the respective CIDR block
# 7. Then we continue looping till n > 0
# 8. What does the function `trailing_0s_digit` do?
#    It's an old trick that gives a number with a single bit in it, the bottom bit that was set in n.
#    At least in two's complement arithmetic, which is just about universal these days.
#    The reason it works: the negative of a number is produced by inverting the number,
#    then adding 1 (that's the definition of two's complement).
#    When you add 1, every bit starting at the bottom that is set will overflow into the next higher bit;
#    this stops once you reach a zero bit. Those overflowed bits will all be zero,
#    and the bits above the last one affected will be the inverse of each other,
#    so the only bit left is the one that stopped the cascade - the one that started as 1 and was inverted to 0.

# P.S. If you're worried about running across one's complement arithmetic here's a version that works with both:

sol = Solution()
assert sol.ipToCIDR(ip="255.0.0.7", n=10) == ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]
