def isprime(n):
    prime = True
    for i in range(2, int(n/2)):
        if n % i == 0:
            prime = False
            break
        return prime

isPrime(17)
