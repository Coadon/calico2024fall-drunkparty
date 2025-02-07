# 2024 Feb 7
# 5. Bridge
# Annotated Solution
# https://github.com/calico-team/calico-fa24/blob/main/bridge/submissions/accepted/binarysearch.py


def solve(B: int, N: int, S: list[int]) -> int:
    '''
    Return the height H in which the danger is minimized and satisfies the budget constraints.
    '''
    lo = min(S)
    hi = max(S)
    # the lower, cost monotonically increase
    # the higher, danger monotonically increase
    # so find going lower will always decrease danger
    # so find the least that is still OK for cost.
    # and also in terms of time, do a binary search.
    while lo < hi:
        # the height of bridge to test for
        mid = (hi - lo) // 2
        cost = 0
        danger = 0
        for h in S:
            # max() will deal with above below naturally
            danger += max(mid - h, 0)
            cost += max(h - mid, 0)
        # restriction
        if cost > B:
            lo = mid
        else:
            hi = mid

    return lo


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]
        print(solve(B, N, S))


if __name__ == '__main__':
    main()
