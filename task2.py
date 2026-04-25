import sys

def is_prime_miller_rabin(n, k=5):
    """Тест Миллера-Рабина на простоту"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Записываем n-1 как 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Свидетели
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    for a in witnesses[:k]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def solve():
    n = int(sys.stdin.readline().strip())
    
    # Используем простые числа в диапазоне [10^5, 10^9]
    # У простого числа только 2 делителя: 1 и само число
    # Вероятность выбрать 1 равна 50%, вероятность выбрать p равна 50%
    # Ожидаемое количество пар с одинаковыми делителями (единицами) очень высокое
    
    result = []
    num = 100003  # Первое нечётное число >= 10^5
    while len(result) < n:
        if is_prime_miller_rabin(num):
            result.append(num)
        num += 2  # Только нечётные числа
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
