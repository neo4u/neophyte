class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product, fraction = 0, 0
        tens_product = 1

        for d1 in reversed(num1):
            tens, fraction = 1, 0

            for d2 in reversed(num2):
                fraction += int(d1) * (tens * int(d2))
                tens *= 10

            product += tens_product * fraction
            tens_product *= 10

        return str(product)

# 456
# 123

# 6 * 3 + 6 * 20 + 6 * 100
# 10 * (5 * 3 + 5 * 20 + 5 * 100)
