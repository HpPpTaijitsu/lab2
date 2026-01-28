from .core import Node, failure, expand
from .queues import FIFOQueue

def breadth_first_search(problem):
    """Поиск в ширину для решения проблемы."""
    node = Node(problem.initial)
    if problem.is_goal(problem.initial):
        return node
    
    frontier = FIFOQueue([node])
    reached = {problem.initial: node}
    
    while frontier:
        node = frontier.pop()
        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.append(child)
    
    return failure