import sys


def parse_input(data):
    connections = {}
    for line in data:
        (a, b) = line.strip().split('-')
        if a not in connections:
            connections[a] = set()
        if b not in connections:
            connections[b] = set()
        connections[a].add(b)
        connections[b].add(a)
    return connections


def count_sets_with_t(computer_connections):
    results = set()
    for (a, bs) in computer_connections.items():
        for b in bs:
            intersection_computers = bs & computer_connections[b]
            if len(intersection_computers) > 0:
                for c in intersection_computers:
                    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                        r = [a, b, c]
                        r.sort()
                        results.add(tuple(r))

    return len(results)


def find_biggest_clique(computer_connections):
    vertices = list(computer_connections.keys())
    vertices.sort()
    cache = set()
    visited = set()
    for vertex in vertices:
        current_vertices = [vertex]
        visited.add(vertex)
        count_max_for(current_vertices, computer_connections[vertex] - visited, computer_connections, cache)
    max_length = 0
    max_clique = ()
    for i in cache:
        if len(i) > max_length:
            max_length = len(i)
            max_clique = i
    return max_clique


def count_max_for(current_vertices, all_visitable_vertices, computer_connections, cache):
    if len(all_visitable_vertices) == 0:
        r = list(current_vertices)
        r.sort()
        cache.add(tuple(r))
    else:
        visited = set()
        for ver in all_visitable_vertices:
            visited.add(ver)
            c_v = current_vertices.copy()
            a_v = all_visitable_vertices.copy() & computer_connections[ver]
            c_v.append(ver)
            count_max_for(c_v, a_v - visited, computer_connections, cache)


test_network = [
    "kh-tc",
    "qp-kh",
    "de-cg",
    "ka-co",
    "yn-aq",
    "qp-ub",
    "cg-tb",
    "vc-aq",
    "tb-ka",
    "wh-tc",
    "yn-cg",
    "kh-ub",
    "ta-co",
    "de-co",
    "tc-td",
    "tb-wq",
    "wh-td",
    "ta-ka",
    "td-qp",
    "aq-cg",
    "wq-ub",
    "ub-vc",
    "de-ta",
    "wq-aq",
    "wq-vc",
    "wh-yn",
    "ka-de",
    "kh-ta",
    "co-tc",
    "wh-qp",
    "tb-vc",
    "td-yn"
]

assert (count_sets_with_t(parse_input(test_network))) == 7
assert(find_biggest_clique(parse_input(test_network))) == ('co','de','ka','ta')

computers_connections = {}
input_data = []
for line in sys.stdin:
    input_data.append(line.strip())

computers_connections = parse_input(input_data)

print(count_sets_with_t(computers_connections))
print(find_biggest_clique(computers_connections))
