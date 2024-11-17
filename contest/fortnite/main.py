
def solve(N: int, H: int, D: int, S: int, P: int) -> int:
    """
    Return the minimum time needed for you to exit the storm.
    
    N: starting health
    H: healing per second
    D: distance out of the storm in meters
    S: running speed in meters per second
    P: storm damage per second
    """
    # Casework
    if (P*D/S <= N):
        # Simpler Case
        return D/S
    elif (P >= H):
        return -1
    else:
        health = D/S*P
        if N < health:
            t = (health-N)/(H-P)
            t = t + D/S
        # impossible case
        # what's the condition?
        return t
        # Complex Case thatt needs healing. Greedy


def main():
    T = int(input())
    for _ in range(T):
        N, H, D, S, P = map(int, input().split()) # u can do thatt??
        print(solve(N, H, D, S, P))

if __name__ == '__main__':
    main()