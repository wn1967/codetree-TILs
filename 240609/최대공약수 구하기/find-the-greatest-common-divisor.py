a,b = map(int, input().split())


def find_gcd(a, b):
    gcd = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    print(gcd)

find_gcd(a, b)