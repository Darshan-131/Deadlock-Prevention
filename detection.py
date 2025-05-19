def detect_deadlock(wait_for_graph):
    visited = set()
    rec_stack = set()

    def dfs(process):
        visited.add(process)
        rec_stack.add(process)
        for neighbor in wait_for_graph.get(process, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(process)
        return False

    for process in wait_for_graph:
        if process not in visited:
            if dfs(process):
                return True
    return False
