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
    
    # Для каждой из 8 спиралей заранее вычислим паттерны
    # spiral_patterns[start_dir][cw][r] = dict {(dx,dy): value}
    
    # Но это займет много памяти. Вместо этого будем проверять инкрементально.
    
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
                            
                            # Длина стороны для спирали: 1,1,2,2,3,3,...
                            actual_steps = layer if side < 2 else layer
                            if side >= 2:
                                actual_steps = layer
                            else:
                                actual_steps = layer
                            
                            # На самом деле для слоя layer:
                            # side 0: layer шагов, side 1: layer шагов
                            # side 2: layer шагов, side 3: layer шагов
                            # Нет, это не так. Давайте посчитаем правильно.
                            
                            # Спираль от центра: 
                            # слой 1: право 1, вниз 1, лево 2, вверх 2 (возврат к строке центра-1)
                            # но нам нужно заполнить квадрат 3x3
                            
                            # Правильная последовательность для заполнения квадрата:
                            # (0,0)=0, затем по спирали наружу
                            # Для 3x3: (0,1)=1, (1,1)=2, (1,0)=3, (1,-1)=4, (0,-1)=5, (-1,-1)=6, (-1,0)=7, (-1,1)=8
                            
                            # Шаги: право 1, вниз 1, лево 2, вверх 2, право 2, ...
                            # Но для квадрата r=1 (3x3), нам нужно 8 шагов после центра
                            
                            # Упрощаем: для слоя layer, каждая сторона имеет length = 2*layer
                            # Но первые две стороны слоя имеют length = 2*layer - 1
                            
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
