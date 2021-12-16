from math import floor, sqrt

def get_counter(n) -> list:
    counters = list()
    for i in range(2,n):
        if n % (i) == 0:
            counters.append(i)
        else: 
            continue

    return counters


def get_prime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return
        else:
            continue

    return 1


def engine(inputs):
    results = list()
    for i in inputs:
        n_primes = 0
        counters = get_counter(i)

        for j in counters:
            flag = get_prime(j)
            if flag:
                n_primes += 1
            else:
                continue

        results.append((i,n_primes))

    sorted_results = sorted(
        results,
        key= lambda x: (x[1], x[0]),
        reverse=True    
    )
    
    output = sorted_results[0]
    print(f"{output[0]} {output[1]}")


inputs = list()

for i in range(10):
    inputs.append(
        int(input())
    )

engine(inputs)


# By Sina Kazemi
# https://github.com/sina96n