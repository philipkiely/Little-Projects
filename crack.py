import hashlib
import random
import sys
import timeit


def encode_num(n):
    r = random.randint(0, 10**n)
    h = hashlib.sha256()
    h.update(str(r).encode())
    return h.hexdigest()


def guess(secret):
    i = 0
    while True:
        h = hashlib.sha256()
        h.update(str(i).encode())
        if h.hexdigest() == secret:
            print(i)
            return
        else:
            i += 1


if __name__ == "__main__":
    start = timeit.default_timer()
    magnitude = int(sys.argv[1])
    secret = encode_num(magnitude)
    guess(secret)
    end = timeit.default_timer()
    print("Time to guess:", end - start)
