common_dict_of_stones_changes = {}  # one and only


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


def blink_25(stones):
    for i in range(25):
        blink(stones)
    next_stone = stones
    stones_length = 0
    while next_stone is not None:
        stones_length += 1
        next_stone = next_stone.next
    return stones_length


def blink(stones):
    next_stone = stones
    while next_stone is not None:
        if int(next_stone.data) == 0:
            next_stone.data = '1'
            next_stone = next_stone.next
        elif len(next_stone.data) % 2 == 0:
            data_string = next_stone.data
            next_stone.data = str(int(data_string[0:int(len(data_string) / 2)]))
            old_next = next_stone.next
            next_stone.next = Node(str(int(data_string[int(len(data_string) / 2):])))
            next_stone.next.next = old_next
            next_stone = old_next
        else:
            next_stone.data = str(int(next_stone.data) * 2024)
            next_stone = next_stone.next
    return stones


def blink_fast(stones_dict, number_of_blinks):
    data_for_blink = stones_dict
    for i in range(number_of_blinks):
        data_for_blink = fast_blink_once(data_for_blink)
    result_stones_number = 0
    for (k, v) in data_for_blink.items():
        result_stones_number += v
    return result_stones_number


def fast_blink_once(stones):
    next_stones = {}
    for (stone, number_of_stones) in stones.items():
        if stone not in common_dict_of_stones_changes:
            if stone == '0':
                common_dict_of_stones_changes['0'] = {'1': 1}
            elif len(stone) % 2 == 0:
                res_dict = {str(int(stone[0:int(len(stone) / 2)])): 1}
                second_part = str(int(stone[int(len(stone) / 2):]))
                if second_part not in res_dict:
                    res_dict[second_part] = 0
                res_dict[second_part] += 1
                common_dict_of_stones_changes[stone] = res_dict
            else:
                common_dict_of_stones_changes[stone] = {str(int(stone) * 2024): 1}

        result_stones = common_dict_of_stones_changes[stone]
        for (result_stone, number_of_result_stones) in result_stones.items():
            if result_stone not in next_stones:
                next_stones[result_stone] = 0
            next_stones[result_stone] = next_stones[result_stone] + (number_of_stones * number_of_result_stones)
    return next_stones


test_stones = Node("125")
test_stones.next = Node("17")
assert blink_25(test_stones) == 55312
assert blink_fast({"125": 1, "17": 1}, 25) == 55312

data = input().strip().split(' ')
stones = Node(data[0])
current = stones
for i in range(1, len(data)):
    current.next = Node(data[i])
    current = current.next

print(blink_25(stones))

stones2 = {}  # number_on_stone -> number_of_such_stones
for i in data:
    if i in stones2:
        stones2[i] = stones2[i] + 1
    else:
        stones2[i] = 1
print(blink_fast(stones2, 75))
