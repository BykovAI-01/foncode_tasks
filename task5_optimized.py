import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    
    grid = []
    for i in range(n):
        row = data[2 + i]
        grid.append([int(c) for c in row])
    
    # Направления: право, вниз, лево, вверх
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    best_area = 1
    best_center = (1, 1)
    
    # Предварительно найдем все нули - потенциальные центры
    zeros = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 0]
    
    # Для каждого центра и каждой из 8 спиралей, находим максимальный радиус
    for cx, cy in zeros:
        max_r = min(cx, n - 1 - cx, cy, n - 1 - cy)
        
        # Для каждой из 8 спиралей
        for start_dir in range(4):
            for cw in [1, -1]:
                r = 1
                while r <= max_r:
                    size = 2 * r + 1
                    area = size * size
                    
                    # Проверяем только новую границу (слой r)
                    valid = True
                    
                    # Генерируем значения для границы размера r
                    x, y = 0, 0
                    curr_val = 1
                    d_idx = start_dir
                    
                    # Проходим все слои от 1 до r
                    for layer in range(1, r + 1):
                        for side in range(4):
                            cur_d = dirs[(start_dir + side * cw) % 4]
                            
                            steps_this_side = 2 * layer
                            if side == 0 or side == 1:
                                steps_this_side = 2 * layer - 1
                            
                            for _ in range(steps_this_side):
                                dx, dy = cur_d
                                x += dx
                                y += dy
                                
                                # Если мы на слое r и на границе
                                if layer == r and max(abs(x), abs(y)) == r:
                                    gx, gy = cx + x, cy + y
                                    if grid[gx][gy] != curr_val:
                                        valid = False
                                        break
                                    curr_val = (curr_val + 1) % k
                            
                            if not valid:
                                break
                            d_idx = (d_idx + cw) % 4
                        
                        if not valid:
                            break
                    
                    if valid:
                        if area > best_area:
                            best_area = area
                            best_center = (cx + 1, cy + 1)
                        r += 1
                    else:
                        break
    
    print(best_area)
    print(best_center[0], best_center[1])

if __name__ == '__main__':
    solve()
