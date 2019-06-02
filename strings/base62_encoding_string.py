def base62_encode(d):
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hash_str = ''
    num_str = ''

    while d:
        i = d % 62
        num_str += ' ' +  str(i)
        hash_str = s[i] + hash_str
        print(f"hash_str: {hash_str} num_str: {num_str} d: {d} i: {i}")
        d //= 62

    return hash_str, num_str

print(base62_encode(99999999998))



# https://stackoverflow.com/questions/1119722/base-62-conversions