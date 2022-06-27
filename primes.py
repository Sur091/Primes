def primes(num):
    dictionary = {}
    for a in range(3, num, 2):
        dictionary[a] = True
    for a in range(3, int(num ** 0.5) + 1, 2):
        if dictionary[a]:
            for b in range(a * a, num, a):
                dictionary[b] = False

    return [2] + [x for x in dictionary if dictionary[x]]


print(len(primes(10000000)))
