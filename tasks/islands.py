from collections import deque

def count_islands(matrix):
    """
    Подсчет количества островов в бинарной матрице.
    Расширенная версия: острова могут соединяться по вертикали, горизонтали и диагонали.
    Матрица: 0 - вода, 1 - земля.
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    
    # Все 8 направлений (включая диагонали)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # верхние: лево, центр, право
        (0, -1),           (0, 1),   # средние: лево, право
        (1, -1),  (1, 0),  (1, 1)    # нижние: лево, центр, право
    ]
    
    def bfs(start_row, start_col):
        """BFS для обхода одного острова."""
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    not visited[nr][nc] and matrix[nr][nc] == 1):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    
    # Подсчет островов
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    return count


def create_custom_matrix():
    """
    Создание собственной матрицы для задания 8.
    В этой матрице будет 6 островов (с учетом диагональных соединений).
    """
    # Собственная матрица 5x5, где 0 - вода, 1 - земля
    custom_matrix = [
        [0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    
    return custom_matrix


def test_islands():
    """
    Тестирование задачи подсчета островов на собственной матрице.
    Используется расширенная версия с учетом диагональных соединений.
    """
    print("="*60)
    print("Задача: Расширенный подсчет количества островов в бинарной матрице")
    print("0 - вода, 1 - земля")
    print("Острова могут соединяться по вертикали, горизонтали и диагонали")
    print("="*60)
    
    # Собственная матрица для задания 8
    matrix = create_custom_matrix()
    
    print("\nМатрица 5x5:")
    for row in matrix:
        print("  " + " ".join(str(cell) for cell in row))
    
    # Подсчет островов
    islands_count = count_islands(matrix)
    
    print(f"\nОбщее количество островов: {islands_count}")
    
    # Детализация островов
    print("\nДетализация островов:")
    
    rows, cols = len(matrix), len(matrix[0])
    island_map = [[0] * cols for _ in range(rows)]
    
    # Используем BFS для разметки каждого острова разными номерами
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = [[False] * cols for _ in range(rows)]
    island_number = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                island_number += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                island_map[i][j] = island_number
                
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and 
                            not visited[nr][nc] and matrix[nr][nc] == 1):
                            visited[nr][nc] = True
                            island_map[nr][nc] = island_number
                            queue.append((nr, nc))
    
    # Вывод детальной информации
    for island_num in range(1, island_number + 1):
        cells = []
        for i in range(rows):
            for j in range(cols):
                if island_map[i][j] == island_num:
                    cells.append(f"({i},{j})")
        print(f"  Остров {island_num}: {', '.join(cells)}")

    print("\n" + "="*60)
    print(f"Итог: в матрице обнаружено {islands_count} островов")
    print("="*60)
    
    return matrix, islands_count


if __name__ == "__main__":
    test_islands()