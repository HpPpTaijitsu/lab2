from search import Problem, breadth_first_search, path_states, failure

# Граф Румынии из первой лабораторной
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}


class RomaniaProblem(Problem):
    """Задача поиска пути в графе Румынии."""
    def __init__(self, initial, goal, graph):
        super().__init__(initial=initial, goal=goal)
        self.graph = graph
    
    def actions(self, state):
        return [city for city, _ in self.graph.get(state, [])]
    
    def result(self, state, action):
        return action
    
    def action_cost(self, s, a, s1):
        for city, cost in self.graph[s]:
            if city == s1:
                return cost
        return float('inf')


def find_shortest_path(start, end):
    """Поиск кратчайшего пути между городами."""
    problem = RomaniaProblem(start, end, romania_map)
    solution = breadth_first_search(problem)
    
    if solution != failure:
        path = path_states(solution)
        print(f"Путь из {start} в {end}:")
        print(" -> ".join(path))
        print(f"Длина пути (в шагах): {len(path)-1}")
        print(f"Общая стоимость: {solution.path_cost}")
        return path, solution.path_cost
    else:
        print(f"Путь из {start} в {end} не найден!")
        return None


def compare_with_manual():
    """Сравнение с ручным решением."""
    print("\n=== Сравнение результатов ===")
    print("Ручное решение (из первой лабы) для Arad -> Bucharest:")
    print("Путь: Arad -> Sibiu -> Fagaras -> Bucharest")
    print("Стоимость: 140 + 99 + 211 = 450")
    print("\nРешение BFS (поиск в ширину):")
    
    path, cost = find_shortest_path('Arad', 'Bucharest')
    
    print("\nВывод: BFS находит путь с минимальным количеством шагов,")
    print("но не обязательно с минимальной стоимостью!")