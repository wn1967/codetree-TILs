def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return lcm(arr[0], lcm_recursive(arr[1:]))

N = int(input())
array = list(map(int, input().split()))

result = lcm_recursive(array)
print(result)