import sys

def solve():
    s = sys.stdin.readline().strip()
    numbers = map(int, s.split('+'))
    result = sum(numbers)
    print(result)

if __name__ == "__main__":
    solve()
