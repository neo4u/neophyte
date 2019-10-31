from typing import List


class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        number = self.ip_to_number(ip)
        print(f"IP: {ip} | Dec: {number}")
        result = []

        while n > 0:
            lowbit = self.lowbit(number)

            while lowbit > n: lowbit //= 2 # Same as right shift by 1 or >>= 1

            r_zeros = self.right_0_bits(lowbit)
            ip = self.number_to_ip(number)
            result.append(f'{ip}/{32 - r_zeros}')
            n -= lowbit
            number += lowbit

        return result

    def ip_to_number(self, ip):
        ip = ip.split('.')
        return (int(ip[0]) << 24) + \
                (int(ip[1]) << 16) + \
                (int(ip[2]) << 8) + \
                int(ip[3])

    def number_to_ip(self, number):
        return '.'.join([
            str(number >> 24 & 255),
            str(number >> 16 & 255),
            str(number >> 8 & 255),
            str(number & 255)
        ])

    def lowbit(self, number):
        return number & -number

    def right_0_bits(self, number):
        count = 0

        while number & 1 == 0:
            count += 1
            number //= 2

        return count
