# 素数判定関数
def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

# 1 から 10 までの範囲内
for n in range(1, 11):
    result = '素数です' if isprime(n) else '素数ではありません'
    print('{}: {}'.format(n, result))