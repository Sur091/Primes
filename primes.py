import numpy as np


def primes(num):
    l_ = (num - 1) // 2
    pri = np.full(l_, True, bool)

    for a in range(int(num ** 0.5) // 2 + 1):
        if pri[a]:
            pri[2 * a * a + 6 * a + 3::2 * a + 3] = False

    return np.sum(pri) + 1


print(primes(1_000_000_000))
