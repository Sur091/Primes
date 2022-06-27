def primes(num):
    l_ = (num - 1) // 2
    pri = [True] * l_

    for a in range(int(num ** 0.5) // 2 + 1):
        if pri[a]:
            start, step = 2 * a * a + 6 * a + 3, 2 * a + 3
            pri[start::step] = [False] * len(range(start, l_, step))

    return sum(pri) + 1


print(primes(100_000_000))
