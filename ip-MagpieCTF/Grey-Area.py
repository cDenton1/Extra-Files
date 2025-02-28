from Crypto.Util.number import long_to_bytes, inverse    # handle converting large number back into og string and modular inverse

p = 961538449797931913175965696759    # p value found through factoring n
q = 967319996044712948532221324531    # q value found through factoring n
e = 0x10001    # 65537

c = 311087069445751882711513305144448403394079226106736563961190    # provided c value
n = 930115369455374918279214292565370334148036289536095273895029    # provided n value
# n could also just be p * q

x = (p - 1) * (q - 1)    # compute x, Euler’s Totient Function, required for computing d
d = inverse(e, x)        # compute modular inverse

m = pow(c, d, n)    # decrypt ciphertext
print(long_to_bytes(m).decode())    # convert m to bytes, and print
