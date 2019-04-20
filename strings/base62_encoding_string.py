def base62_encode(d):
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hash_str = ''
    num_str = ''

    while d:
        num_str += ' ' +  str(d % 62)
        hash_str += s[d % 62]
        d //= 62

    return hash_str, num_str

print(base62_encode(99999999998))

# https://stackoverflow.com/questions/1119722/base-62-conversions