from collections import deque

def count_islands(matrix, diagonal=False):
    """
    Подсчет количества островов в бинарной матрице.
    Остров - группа единиц (1), соединенных по горизонтали/вертикали (или диагоналям).
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    
    # Направления движения
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
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


def test_islands():
    """Тестирование на примере из методички."""
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1]
    ]
    
    print("Матрица островов:")
    for row in matrix:
        print(row)
    
    print(f"\nКоличество островов (без диагоналей): {count_islands(matrix, diagonal=False)}")
    print(f"Количество островов (с диагоналями): {count_islands(matrix, diagonal=True)}")
    
    return matrix

def create_custom_matrix():
    """Создание собственной матрицы для тестирования."""
    custom_matrix = [
        [1, 1, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]
    return custom_matrix