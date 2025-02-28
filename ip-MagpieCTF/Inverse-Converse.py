from Crypto.Util.number import long_to_bytes, inverse    # handle converting large number back into og string and modular inverse

# provided c and k values
c = 4082963394707349379691940087749373560022452272321719622709503732828753479223853620855771
k = 59936462153071551643692430070494658880579757984426138973968053464181955001212203124978301
n = 0x1337    # 4919

x = inverse(n, k)    # compute modular inverse
m = (c * x) % k      # solve for m and recover the original message

flag = long_to_bytes(m)  # convert m to bytes to get the flag
print(flag.decode())     # print the flag
