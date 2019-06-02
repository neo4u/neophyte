def binary_convert(d):
    bin_str = ""

    while d:
        i = d % 2
        bin_str = str(i) + bin_str
        d //= 2

    return bin_str

print(binary_convert(100))