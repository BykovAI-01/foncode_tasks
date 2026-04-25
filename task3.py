import sys
import math

def solve():
    line = sys.stdin.readline().strip()
    parts = list(map(int, line.split()))
    a, b, c = parts[0], parts[1], parts[2]
    x, y = parts[3], parts[4]
    
    # Расстояние от начала координат до целевой точки
    dist = math.sqrt(x * x + y * y)
    
    # Максимальное расстояние, которое может достичь рука
    max_reach = a + b + c
    
    # Минимальное расстояние (когда сегменты складываются)
    # Рука может достичь любую точку в диапазоне [min_reach, max_reach]
    # где min_reach = max(0, max_segment - sum_of_others)
    
    segments = sorted([a, b, c], reverse=True)
    max_seg = segments[0]
    sum_others = segments[1] + segments[2]
    
    if max_seg > sum_others:
        min_reach = max_seg - sum_others
    else:
        min_reach = 0
    
    # Проверяем, лежит ли расстояние в допустимом диапазоне
    if min_reach <= dist <= max_reach:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
