from collections import deque


def shortest_path_in_maze(maze, start, end):
    """
    Поиск кратчайшего пути в лабиринте с использованием BFS.
    Лабиринт: 1 - проход, 0 - стена.
    Возвращает длину кратчайшего пути или -1, если путь не найден.
    """
    if not maze or not maze[0]:
        return -1, []

    rows, cols = len(maze), len(maze[0])

    # Проверка начальной и конечной точек
    if (
        start[0] < 0
        or start[0] >= rows
        or start[1] < 0
        or start[1] >= cols
        or end[0] < 0
        or end[0] >= rows
        or end[1] < 0
        or end[1] >= cols
    ):
        return -1, []

    if maze[start[0]][start[1]] == 0 or maze[end[0]][end[1]] == 0:
        return -1, []

    # Направления движения: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Очередь для BFS: (row, col, distance)
    queue = deque([(start[0], start[1], 0)])

    # Массив для отслеживания посещенных клеток
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    # Массив для хранения предыдущей клетки (для восстановления пути)
    parent = [[None] * cols for _ in range(rows)]

    while queue:
        row, col, distance = queue.popleft()

        # Если достигли конечной точки
        if (row, col) == end:
            # Восстановление пути
            path = []
            r, c = row, col
            while (r, c) != start:
                path.append((r, c))
                r, c = parent[r][c]
            path.append(start)
            path.reverse()

            return distance, path

        # Проверяем все возможные направления
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Проверка границ и доступности клетки
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and maze[new_row][new_col] == 1
                and not visited[new_row][new_col]
            ):
                visited[new_row][new_col] = True
                parent[new_row][new_col] = (row, col)
                queue.append((new_row, new_col, distance + 1))

    return -1, []  # Путь не найден


def create_custom_maze():
    """
    Создание лабиринта.
    Лабиринт 8x8: 1 - проход, 0 - стена
    """
    custom_maze = [
        [1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 1],
    ]

    start = (0, 0)
    end = (7, 7)

    return custom_maze, start, end


def test_maze():
    """
    Тестирование задачи поиска кратчайшего пути в лабиринте.
    """
    print("=" * 60)
    print("Задача: Поиск кратчайшего пути в лабиринте")
    print("1 - проход, 0 - стена")
    print("=" * 60)

    print("\nЛабиринт (8x8):")

    maze, start, end = create_custom_maze()

    # Вывод матрицы лабиринта
    for row in maze:
        print("  " + " ".join(str(cell) for cell in row))

    print(f"\nНачальная точка: {start}")
    print(f"Конечная точка: {end}")

    # Поиск кратчайшего пути
    result, path = shortest_path_in_maze(maze, start, end)

    if result != -1:
        print(f"\nДлина кратчайшего пути: {result}")

        # Визуализация пути
        print("\nВизуализация пути:")
        print("S - старт, E - конец, P - путь, " "█ - стена, · - проход")

        visual = []
        for i in range(len(maze)):
            visual_row = []
            for j in range(len(maze[0])):
                if (i, j) == start:
                    visual_row.append("S")
                elif (i, j) == end:
                    visual_row.append("E")
                elif (i, j) in path:
                    visual_row.append("P")
                else:
                    visual_row.append("█" if maze[i][j] == 0 else "·")
            visual.append(visual_row)

        for row in visual:
            print("  " + " ".join(row))

        # Вывод последовательности координат пути
        print(f"\nПоследовательность координат пути " f"({len(path)} точек):")
        for i, (r, c) in enumerate(path):
            print(f"  Шаг {i:2d}: ({r}, {c})")
    else:
        print("\nПуть не найден!")

    print("\n" + "=" * 60)
    print(f"Итог: длина кратчайшего пути = {result}")
    print("=" * 60)

    return maze, start, end, result, path


if __name__ == "__main__":
    test_maze()
