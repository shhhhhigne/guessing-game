def is_prime(num):
    for i in xrange(2, num):
        if num % i == 0:
            return False
    return True


def prime_count(count):
    result = []
    n = 2
    while len(result) < count:
        if is_prime(n):
            result.append(n)
        n += 1
    print result


prime_count(5)
