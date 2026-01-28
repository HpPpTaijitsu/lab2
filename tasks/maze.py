from search import Problem, breadth_first_search, path_states, failure
from collections import deque

class MazeProblem(Problem):
    """Задача поиска пути в лабиринте."""
    def __init__(self, initial, goal, maze):
        super().__init__(initial=initial, goal=goal)
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0]) if self.rows > 0 else 0
    
    def actions(self, state):
        """Возможные движения в лабиринте."""
        r, c = state
        moves = []
        # Вверх, вниз, влево, вправо
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < self.rows and 0 <= nc < self.cols and 
                self.maze[nr][nc] == 0):  # 0 - проход
                moves.append((nr, nc))
        return moves
    
    def result(self, state, action):
        return action
    
    def action_cost(self, s, a, s1):
        return 1


def solve_maze(maze, start, end):
    """Решение лабиринта с помощью BFS."""
    problem = MazeProblem(start, end, maze)
    solution = breadth_first_search(problem)
    
    if solution != failure:
        return path_states(solution)
    return None


def test_maze():
    """Тестирование на примере лабиринта."""
    maze = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    end = (4, 5)
    
    print("Лабиринт (0-проход, 1-стена):")
    for i, row in enumerate(maze):
        row_str = []
        for j, cell in enumerate(row):
            if (i, j) == start:
                row_str.append('S')
            elif (i, j) == end:
                row_str.append('E')
            else:
                row_str.append(str(cell))
        print(' '.join(row_str))
    
    path = solve_maze(maze, start, end)
    
    if path:
        print(f"\nНайден путь длиной {len(path)-1} шагов:")
        for step in path:
            print(f"  {step}")
    else:
        print("\nПуть не найден!")
    
    return maze, start, end, path

def create_custom_maze():
    """Создание собственного лабиринта."""
    custom_maze = [
        [0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    return custom_maze