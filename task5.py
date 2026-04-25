import sys

def solve():
    line = sys.stdin.readline().strip()
    n, k = map(int, line.split())
    
    # Читаем таблицу
    grid = []
    for _ in range(n):
        row = sys.stdin.readline().strip()
        grid.append([int(c) for c in row])
    
    # 8 направлений для первого шага из центра
    # dx, dy: right, down, left, up
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def check_snake(cx, cy, max_radius):
        """Проверяет максимальный радиус змейки с центром (cx, cy)"""
        if grid[cx][cy] != 0:
            return 0
        
        # Проверяем все 8 комбинаций (4 начальных направления * 2 направления вращения)
        best_radius = 0
        
        for start_dir in range(4):
            for clockwise in [True, False]:
                radius = check_pattern(cx, cy, start_dir, clockwise, max_radius)
                if radius > best_radius:
                    best_radius = radius
        
        return best_radius
    
    def check_pattern(cx, cy, start_dir, clockwise, max_possible):
        """Проверяет паттерн змейки и возвращает максимальный радиус"""
        # Порядок направлений
        if clockwise:
            dir_order = [(start_dir + i) % 4 for i in range(4)]
        else:
            dir_order = [(start_dir - i) % 4 for i in range(4)]
        
        x, y = cx, cy
        seg_len = 1
        seg_idx = 0
        step = 0  # Номер шага (не включая центр)
        
        max_steps = (2 * max_possible + 1) ** 2 - 1
        
        while step < max_steps:
            d = dir_order[seg_idx % 4]
            
            # Проходим сегмент длины seg_len
            for _ in range(seg_len):
                if step >= max_steps:
                    break
                    
                x += dx[d]
                y += dy[d]
                
                # Проверка границ
                if x < 0 or x >= n or y < 0 or y >= n:
                    # Возвращаем текущий достигнутый радиус
                    current_radius = int((step ** 0.5) / 2) + 1
                    return min(current_radius, max_possible)
                
                expected = (step + 1) % k
                if grid[x][y] != expected:
                    # Возвращаем максимальный радиус, который удалось достичь
                    # Размер квадрата = 2*radius + 1, где radius - это расстояние от центра до края
                    # step - это количество пройденных клеток после центра
                    # Для радиуса r, нужно пройти (2r+1)^2 - 1 шагов
                    # Ищем максимальное r такое, что (2r+1)^2 - 1 <= step
                    if step == 0:
                        return 0
                    # Приближённо: radius ≈ sqrt(step) / 2
                    # Но точнее: для полного квадрата размера 2r+1 нужно (2r+1)^2 - 1 шагов
                    # Если мы прошли step шагов, то максимальный полный квадрат имеет размер
                    # такой, что (2r+1)^2 - 1 <= step
                    r = 0
                    for test_r in range(1, max_possible + 1):
                        needed = (2 * test_r + 1) ** 2 - 1
                        if needed <= step:
                            r = test_r
                        else:
                            break
                    return r
                
                step += 1
            
            seg_idx += 1
            if seg_idx % 2 == 0:
                seg_len += 1
        
        return max_possible
    
    # Перебираем все возможные центры
    best_size = 1
    best_center = None
    
    # Сначала найдём хотя бы одну змейку размера 1 (клетка с 0)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                best_size = 1
                best_center = (i + 1, j + 1)
    
    # Перебираем все центры и проверяем максимальный размер змейки
    for cx in range(n):
        for cy in range(n):
            if grid[cx][cy] != 0:
                continue
            
            # Максимально возможный радиус для этого центра
            max_radius = min(cx, cy, n - 1 - cx, n - 1 - cy)
            
            if max_radius == 0:
                continue
            
            radius = check_snake(cx, cy, max_radius)
            size = 2 * radius + 1
            
            if size > best_size:
                best_size = size
                best_center = (cx + 1, cy + 1)
    
    print(best_size * best_size)
    print(best_center[0], best_center[1])

if __name__ == "__main__":
    solve()
