from collections import deque


def water_jugs_bfs(initial, goal, sizes):
    """
    Решение задачи о льющихся кувшинах с использованием BFS.
    """

    def apply_action(state, action):
        new_state = list(state)

        if action[0] == "Fill":
            _, i = action
            new_state[i] = sizes[i]

        elif action[0] == "Dump":
            _, i = action
            new_state[i] = 0

        elif action[0] == "Pour":
            _, i, j = action
            amount = min(state[i], sizes[j] - state[j])
            new_state[i] = state[i] - amount
            new_state[j] = state[j] + amount

        return tuple(new_state)

    def generate_actions(state, num_jugs):
        actions = []

        for i in range(num_jugs):
            if state[i] < sizes[i]:
                actions.append(("Fill", i))

        for i in range(num_jugs):
            if state[i] > 0:
                actions.append(("Dump", i))

        for i in range(num_jugs):
            for j in range(num_jugs):
                if i != j and state[i] > 0 and state[j] < sizes[j]:
                    actions.append(("Pour", i, j))

        return actions

    num_jugs = len(initial)

    if goal in initial:
        return [], [initial]

    queue = deque()
    queue.append((initial, []))
    visited = {initial}

    while queue:
        current_state, actions_path = queue.popleft()
        possible_actions = generate_actions(current_state, num_jugs)

        for action in possible_actions:
            new_state = apply_action(current_state, action)

            if new_state in visited:
                continue

            new_actions_path = actions_path + [action]

            if goal in new_state:
                states_path = [initial]
                current_state_path = initial
                for act in new_actions_path:
                    current_state_path = apply_action(current_state_path, act)
                    states_path.append(current_state_path)

                return new_actions_path, states_path

            visited.add(new_state)
            queue.append((new_state, new_actions_path))

    return [], []


def run_example_only():
    """
    Реализация примера из условия задачи
    """
    print("=" * 60)
    print("Задача о льющихся кувшинах")
    print("=" * 60)

    initial = (1, 1, 1)
    goal = 13
    sizes = (2, 16, 32)

    print(f"Начальное состояние: {initial}")
    print(f"Целевой объем: {goal}")
    print(f"Емкости кувшинов: {sizes}")
    print()

    actions, states = water_jugs_bfs(initial, goal, sizes)

    if actions:
        print("Последовательность действий:")
        print(actions)

        print("\nПоследовательность состояний:")
        print(states)

        print(
            f"\nИтог: достигнут объем {goal} "
            f"в кувшине {states[-1].index(goal)}"
        )
    else:
        print("Решение не найдено!")

    return actions, states


if __name__ == "__main__":
    run_example_only()
