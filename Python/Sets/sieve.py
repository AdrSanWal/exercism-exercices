def primes(limit):
    prime = [True for i in range(limit + 1)]
    num = 2
    while (num * num <= limit):
        if prime[num]:
            for i in range(num * num, limit + 1, num):
                prime[i] = False
        num += 1
    return [num for num in range(2, limit + 1) if prime[num]]
