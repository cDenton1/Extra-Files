from Crypto.Util.number import long_to_bytes, inverse
from sympy import primerange

n = 796619421721763408110066621894301379640702094358332972179336180714381814791  # replace with provided value
e = 65537                                                                        # replace with provided value
c = 760460476332603195975870956320663031030142509238270316470240866540546100772  # replace with provided value

# Brute-force factor n using all 16-bit primes
primes = []
remaining = n

for p in primerange(2**15, 2**16):  # 16-bit primes range
    while remaining % p == 0:
        primes.append(p)
        remaining //= p
        if len(primes) == 16:
            break
    if len(primes) == 16:
        break

assert len(primes) == 16, "Did not find 16 prime factors"

# Compute phi
phi = 1
for p in primes:
    phi *= (p - 1)

# Compute private key
d = inverse(e, phi)

# Decrypt
m = pow(c, d, n)
flag = long_to_bytes(m)
print(flag)
