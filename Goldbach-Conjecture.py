import math

n = int(input("Provide an even number: "))
factors_n = []
n_pow = math.pow(n, math.inf)

for i in range(1, n + 1):
    if n % i == 0:
        factors_n.append(i)

if n % 2 == 0 and n > 2 and n < n ** n_pow:
    second_highest_factor = factors_n[-2]

    prime1 = second_highest_factor
    prime2 = prime1

    for j in range(n, n ** 5 + 1, 2):
        is_prime1 = True

        for num1 in range(2, int(prime1 ** 0.5) + 1):
            if prime1 % num1 == 0:
                is_prime1 = False
                break

        if is_prime1:
            print(j, "=", prime1, "+", prime2)

        prime1 += 2
