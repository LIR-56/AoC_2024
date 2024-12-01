import sys


def total_distance(list_a, list_b):
    list_a.sort()
    list_b.sort()
    elements_sum = 0
    for a, b in zip(list_a, list_b):
        elements_sum += abs(a - b)
    return elements_sum

def similarity_score(list_a, list_b):
    i = 0
    j = 0
    list_a.sort()
    list_b.sort()
    counted_dict = dict.fromkeys(list_a)
    sim_score = 0
    current_elem_amount = 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] == list_b[j]:
            current_elem_amount += 1
            j += 1
        else:
            if current_elem_amount > 0:
                counted_dict[list_a[i]] = current_elem_amount
                sim_score += current_elem_amount * list_a[i]
                current_elem_amount = 0
            if list_a[i] < list_b[j]:
                i += 1
                while i < len(list_a) and list_a[i] == list_a[i - 1]:
                    if counted_dict[list_a[i]] is not None:
                        sim_score += counted_dict[list_a[i]] * list_a[i]
                    i += 1
            else:
                j += 1

    if i < len(list_a):
        sim_score += current_elem_amount * list_a[i]
        counted_dict[list_a[i]] = current_elem_amount
        i += 1
    while i < len(list_a):
        if counted_dict[list_a[i]] is not None:
            sim_score += counted_dict[list_a[i]] * list_a[i]
        i += 1
    return sim_score

assert total_distance([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 11
assert similarity_score([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 31

list_1 = []
list_2 = []

for line in sys.stdin:
    el_1, el_2 = line.split()
    list_1.append(int(el_1))
    list_2.append(int(el_2))
print(total_distance(list_1, list_2))
print(similarity_score(list_1, list_2))
