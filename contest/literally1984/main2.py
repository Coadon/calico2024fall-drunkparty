import math

def solve(N: int) -> list[int]:
    """
    Return a tuple containing the coordinates X and Y.

    N: a positive integer, the address of your house
    """
    # memoize later

    address = 0
    d = 0
    while True:
        # d loop
        d += 1
        for x in range(1,d+1):
            y = d + 1 - x
            if (math.gcd(x, y) == 1):
                address += 1
            if (address == N):
                return [x, y]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(*solve(N))


if __name__ == "__main__":
    main()
