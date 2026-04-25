import sys

def solve():
    line = sys.stdin.readline().strip()
    n, k = map(int, line.split())
    
    # Читаем таблицу
    grid = []
    for _ in range(n):
        row = sys.stdin.readline().strip()
        grid.append([int(c) for c in row])
    
    # 8 направлений спирали (по часовой и против часовой стрелки)
    # Для змейки размера m, мы начинаем с центра и идём по спирали
    
    # Направления для спирали по часовой стрелке: право, низ, лево, верх
    # Направления для спирали против часовой стрелки: право, верх, лево, низ
    # Но на самом деле есть 8 возможных начальных направлений и 2 направления вращения
    
    # Упрощение: для каждой клетки как потенциального центра, проверяем все 8 возможных змеек
    
    # 8 паттернов змеек размера 3 (направления первого шага и вращения):
    # Первый шаг может быть в любом из 4 направлений, и есть 2 направления вращения
    
    # Directions: right, down, left, up
    dx = [0, 1, 0, -1]  # right, down, left, up
    dy = [1, 0, -1, 0]
    
    def check_snake(cx, cy, size):
        """Проверяет, является ли квадрат размера size с центром (cx, cy) змейкой"""
        if size == 1:
            return grid[cx][cy] == 0
        
        # Радиус от центра до края
        radius = size // 2
        
        # Проверяем все 8 комбинаций (4 начальных направления * 2 направления вращения)
        for start_dir in range(4):
            for clockwise in [True, False]:
                if check_snake_pattern(cx, cy, size, start_dir, clockwise):
                    return True
        
        return False
    
    def check_snake_pattern(cx, cy, size, start_dir, clockwise):
        """Проверяет конкретный паттерн змейки"""
        radius = size // 2
        
        # Генерируем координаты спирали
        x, y = cx, cy
        
        # Проверяем центр
        if grid[x][y] != 0:
            return False
        
        # Направления движения по спирали
        # Спираль: право, вниз, влево, вверх, право, ... (по часовой)
        # или право, вверх, влево, вниз, право, ... (против часовой)
        
        dirs = list(range(4))
        if not clockwise:
            dirs = [0, 3, 2, 1]  # right, up, left, down
        
        # Смещаем начала направлений
        dirs = [(start_dir + i) % 4 for i in range(4)]
        if not clockwise:
            dirs = [(start_dir - i) % 4 for i in range(4)]
        
        expected = 0
        x, y = cx, cy
        
        # Длина каждого сегмента спирали: 1, 1, 2, 2, 3, 3, ...
        # Но для змейки размера m, мы идём radius раз в каждом направлении
        
        # Более простой подход: генерируем координаты по спирали
        spiral_coords = generate_spiral_coords(cx, cy, radius, start_dir, clockwise)
        
        for idx, (nx, ny) in enumerate(spiral_coords):
            expected = (idx + 1) % k
            if grid[nx][ny] != expected:
                return False
        
        return True
    
    def generate_spiral_coords(cx, cy, radius, start_dir, clockwise):
        """Генерирует координаты спирали от центра до радиуса radius"""
        coords = []
        
        x, y = cx, cy
        
        # Длины сегментов: 1, 1, 2, 2, 3, 3, ..., radius, radius
        # Но нам нужно покрыть квадрат размера 2*radius+1
        
        # Порядок направлений
        if clockwise:
            dir_order = [(start_dir + i) % 4 for i in range(4)]
        else:
            dir_order = [(start_dir - i) % 4 for i in range(4)]
        
        seg_len = 1
        seg_idx = 0
        
        while len(coords) < (2 * radius + 1) ** 2 - 1:
            d = dir_order[seg_idx % 4]
            
            # Длина текущего сегмента
            current_len = seg_len
            
            for _ in range(current_len):
                x += dx[d]
                y += dy[d]
                
                # Проверка границ
                if x < 0 or x >= n or y < 0 or y >= n:
                    return coords
                
                coords.append((x, y))
                
                if len(coords) >= (2 * radius + 1) ** 2 - 1:
                    break
            
            if len(coords) >= (2 * radius + 1) ** 2 - 1:
                break
            
            seg_idx += 1
            if seg_idx % 2 == 0:
                seg_len += 1
        
        return coords[:radius * (radius + 1) * 2]  # Приблизительно
    
    # Перебираем все возможные центры и размеры
    best_size = 1
    best_center = None
    
    # Сначала найдём хотя бы одну змейку размера 1 (клетка с 0)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                best_size = 1
                best_center = (i + 1, j + 1)
                break
        if best_center:
            break
    
    # Перебираем нечётные размеры от 3 до n
    for size in range(3, n + 1, 2):
        radius = size // 2
        
        for cx in range(radius, n - radius):
            for cy in range(radius, n - radius):
                if check_snake(cx, cy, size):
                    if size > best_size:
                        best_size = size
                        best_center = (cx + 1, cy + 1)
    
    print(best_size * best_size)
    print(best_center[0], best_center[1])

if __name__ == "__main__":
    solve()
