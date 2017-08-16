# from time to time i need to figure out Fixnum::MAX, Fixnum::MIN (aka
# Integer::MAX, Integer::MIN) in ruby and always forget how.  this is how.
#

class Integer
  N_BYTES = [42].pack('i').size
  N_BITS = N_BYTES * 8
  MAX = 2 ** (N_BITS - 2) - 1
  MIN = -MAX - 1
end

p(Integer::MAX)             #=> 1073741823
p(Integer::MAX.class)       #=> Fixnum
p((Integer::MAX + 1).class) #=> Bignum

p(Integer::MIN)             #=> -1073741824
p(Integer::MIN.class)       #=> Fixnum
p((Integer::MIN - 1).class) #=> Bignum