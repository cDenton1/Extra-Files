from Crypto.Util.number import long_to_bytes    # handle converting large number back into og string
import gmpy2                                    # handle math and large operations

# provided c value, encrypted message using RSA
c = 121097813989638138346058726004363325645055007528244635971148694227865847570370087018045267126514696616744216943938638911580999312232908265654986785392772317303161096833644079741186123067589808986604522528602623394273539018995365633

m = gmpy2.iroot(c, 3)[0]        # compute cube root of c

flag = long_to_bytes(int(m))    # convert back to readable bytes
print(flag.decode())            # print out the plaintext (flag)
