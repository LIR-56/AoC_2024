import sys


class LinkedList:
    def __init__(self):
        self.last = None
        self.first = None

    def __repr__(self):
        cur = self.first
        result = []
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

    def get_as_list(self):
        return self.__repr__()

    def __add__(self, other):
        if self.first is None:
            self.first = Node(other)
            self.last = self.first
        else:
            self.last.next = Node(other)
            self.last = self.last.next
        return self

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node
            node = node.next

    def pop(self):
        removing = self.first
        if removing is not None:
            self.first = self.first.next
        if self.first is None:
            self.last = None
        return removing


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sum_of_2000th_steps(secret_numbers):
    cache = {}
    result = []
    for secret_number in secret_numbers:
        current = secret_number
        for i in range(2000):
            if current in cache:
                current = cache[current]
            else:
                next = calculate_next_secret_number(current)
                cache[current] = next
                current = next
        result.append(current)
    return sum(result)


def calculate_next_secret_number(number):
    v1 = prune(mix(number, number * 64))
    v2 = prune(mix(v1, v1 // 32))
    return prune(mix(v2, v2 * 2048))


def mix(secret_number, num):
    return secret_number ^ num


def prune(secret_number):
    return secret_number % 16777216


def find_most_bananas(secret_numbers):
    cache = {}
    changes_dict_of_bananas = {}
    for secret_number in secret_numbers:
        current = secret_number
        changes = {}
        llist = LinkedList()
        llist += secret_number
        for i in range(4):
            if current in cache:
                next = cache[current]
            else:
                next = calculate_next_secret_number(current)
                cache[current] = next
            llist += next
            current = next

        for i in range(2000 - 4):
            ch = list(map(lambda x: x % 10, llist.get_as_list()))
            assert len(ch) == 5
            diff = (ch[1] - ch[0], ch[2] - ch[1], ch[3] - ch[2], ch[4] - ch[3])
            value = ch[4]
            if diff not in changes:
                changes[diff] = value
            if current in cache:
                next = cache[current]
            else:
                next = calculate_next_secret_number(current)
                cache[current] = next
            llist += next
            current = next
            llist.pop()
        for (change, diff) in changes.items():
            if change in changes_dict_of_bananas:
                changes_dict_of_bananas[change].append(diff)
            else:
                changes_dict_of_bananas[change] = [diff]
    max_bananas = 0
    for values in changes_dict_of_bananas.values():
        s = sum(values)
        if s > max_bananas:
            max_bananas = s
    return max_bananas


assert mix(42, 15) == 37
assert prune(100000000) == 16113920
assert sum_of_2000th_steps([1, 10, 100, 2024]) == 37327623
assert find_most_bananas([1, 2, 3, 2024]) == 23

start_secret_numbers = []
for line in sys.stdin:
    start_secret_numbers.append(int(line.strip()))
print(sum_of_2000th_steps(start_secret_numbers))
print(find_most_bananas(start_secret_numbers))
