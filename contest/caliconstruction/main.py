import math

def solve():
    count: dict = { 'C': 0, 'A': 0, 'L': 0, 'I': 0, 'O': 0 }
    S = input()
    for c in S:
        if (c == 'C' or c == 'U' or c == 'N'):
            count['C'] += 1
        elif (c == 'A'):
            count['A'] += 1
        elif (c == 'L'):
            count['L'] += 1
        elif (c == 'I' or c == 'H'):
            count['I'] += 1
        elif (c == 'O'):
            count['O'] += 1
        else:
            print(-1)
            return
    c = math.ceil(count['C'] / 2)
    print(max(c, count['A'], count['I'], count['L'], count['O']))
    return


if __name__ == "__main__":
    T = int(input())
    for TC in range(0,T):
        solve()
