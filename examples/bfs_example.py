from search import Problem, breadth_first_search, path_states

# Простой граф для примера
simple_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

class SimpleGraphProblem(Problem):
    def __init__(self, initial, goal, graph):
        super().__init__(initial=initial, goal=goal)
        self.graph = graph
    
    def actions(self, state):
        return self.graph.get(state, [])
    
    def result(self, state, action):
        return action
    
    def action_cost(self, s, a, s1):
        return 1


def run_example():
    """Запуск примера BFS на простом графе."""
    print("Пример BFS на простом графе:")
    print("Граф: A -> B, C; B -> D, E; C -> F; E -> F")
    
    problem = SimpleGraphProblem('A', 'F', simple_graph)
    solution = breadth_first_search(problem)
    
    if solution:
        path = path_states(solution)
        print(f"Найден путь: {' -> '.join(path)}")
        print(f"Длина пути: {len(path)-1} шагов")
    else:
        print("Путь не найден!")