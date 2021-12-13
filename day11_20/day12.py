from collections import defaultdict

def part1():

    graph = defaultdict(list)

    with open('day12.txt') as file:
        for line in file.read().splitlines():
            src, dst = line.split('-')
            graph[src].append(dst)
            graph[dst].append(src)

    smalls = set()

    def paths_to_end(node='start'):
        if node == 'end':
            return 1
        if node in smalls:
            return 0
        if node.islower():
            smalls.add(node)
        count = sum(paths_to_end(neighbor) for neighbor in graph[node])
        if node.islower():
            smalls.remove(node)
        
        return count

    print(paths_to_end())

def part2():
    d = defaultdict(set)

    with open('day12.txt') as f:
        for line in f:
            a, b = line.rstrip('\n').split('-')
            if b != 'start' and a != 'end':
                d[a].add(b)
            if b != 'end' and a != 'start':
                d[b].add(a)

    def is_small(s: str) -> bool:
        return s[0].islower()

    class Visitor:
        def __init__(self, has_twice, visited) -> None:
            self.has_twice = has_twice
            self.visited = visited

        def can_visit(self, node: str) -> bool:
            return not is_small(node) or not self.has_twice or node not in self.visited

        def after_visit(self, node: str):
            return Visitor(self.has_twice, self.visited) if not is_small(node) else Visitor(self.has_twice or node in self.visited, {node, *self.visited})

    def dfs(node: str, visitor: Visitor) -> int:
        return 1 if node == 'end' else sum(dfs(next_node, visitor.after_visit(next_node)) for next_node in d[node] if visitor.can_visit(next_node))

    print(dfs('start', Visitor(False, {'start'})))

part2()