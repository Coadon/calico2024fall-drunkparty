import math

def gcd(a,b) -> int:                              #gcd(a,b)
    if b==0:
        return a
    else:
        return gcd(b,a%b)

# cache: dict = { 1, (1,1) }
# cache_top = 1

def solve(N: int) -> list[int]:
    """
    Return a tuple containing the coordinates X and Y.

    N: a positive integer, the address of your house
    """
    # memoize later

    # if (N <= cache_top):
    #     top = cache[N]
    #     return [top[0], top[1]]

    # top = cache[cache_top]
    # address = cache_top
    # d = top[1] + top[0]
    address = 0
    d = 0
    while True:
        d += 1
        for x in range(1,d+1):
            y = d + 1 - x
            if (gcd(x, y) == 1):
                address += 1
                # cache[address] = (x,y)
                # cache_top = address
            if (address == N):
                return [x, y]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(*solve(N))


if __name__ == "__main__":
    main()
