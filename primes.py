def primes(num):
    lst = [2]

    for a in range(3, num, 2):
        pri = True
        for b in range(3, int(a ** 0.5) + 1, 2):
            if a % b == 0:
                pri = False
                break
        if pri:
            lst.append(a)
    return lst


print(len(primes(1000000)))
