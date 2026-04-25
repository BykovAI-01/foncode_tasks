import sys

def solve():
    n = int(sys.stdin.readline())
    
    # Используем простые числа >= 100000
    # У простого числа p делители {1, p}, вероятность выбрать 1 = 1/2
    # Ожидаемое число пар: n*(n-1)/8 >= 5n при n >= 41
    # При n >= 80 вероятность провала крайне мала
    
    # Быстрая генерация простых чисел решетом Эратосфена
    LIMIT = 1500000
    is_prime = bytearray([1]) * LIMIT
    is_prime[0] = is_prime[1] = 0
    
    for i in range(2, int(LIMIT**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i:LIMIT:i] = bytearray([0]) * len(range(i*i, LIMIT, i))
    
    primes = [i for i in range(100000, LIMIT) if is_prime[i]]
    
    result = primes[:n]
    print(*result)

if __name__ == '__main__':
    solve()
