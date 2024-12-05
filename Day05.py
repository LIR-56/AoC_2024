import sys


def sum_of_middle_page_numbers_from_correct_updates(rules_list, updates_list):
    result = 0
    rules_dict = get_rules_dict(rules_list)
    for update in updates_list:
        if is_update_correct_ordered(rules_dict, update):
            result += update[int(len(update) / 2)]
    return result


def get_rules_dict(rules_list):
    rules_dict = {}
    for rule in rules_list:
        if not rule[0] in rules_dict:
            rules_dict[rule[0]] = set()
        rules_dict[rule[0]].add(rule[1])
    return rules_dict


def get_reverse_rules_dict(rules_list):
    reverse_rules_dict = {}
    for rule in rules_list:
        if not rule[1] in reverse_rules_dict:
            reverse_rules_dict[rule[1]] = set()
        reverse_rules_dict[rule[1]].add(rule[0])
    return reverse_rules_dict


def is_update_correct_ordered(rules_dict, update):
    updated_pages = set()
    for i in update:
        if i in rules_dict:
            for j in rules_dict[i]:
                if j in updated_pages:
                    return False
        updated_pages.add(i)
    return True


def sum_of_middle_page_numbers_for_corrected_updates(rules_list, updates_list):
    incorrect_updates = []
    corrected_updates = []
    result = 0
    rules_dict = get_rules_dict(rules_list)
    reverse_rules_dict = get_reverse_rules_dict(rules_list)

    for update in updates_list:
        if not is_update_correct_ordered(rules_dict, update):
            incorrect_updates.append(update)

    for incorrect_update in incorrect_updates:
        corrected = correct_update(reverse_rules_dict, incorrect_update)
        corrected_updates.append(corrected)
        result += corrected[int(len(corrected) / 2)]
    return result


def correct_update(reverse_rules_dict, update):
    result = []
    local_rev_dict = {}
    for i in update:
        if not i in reverse_rules_dict:
            local_rev_dict[i] = set()
        else:
            local_rev_dict[i] = reverse_rules_dict[i].intersection(update)

    while len(result) != len(update):
        element = 0
        for (k, v) in local_rev_dict.items():
            if len(v) == 0:
                result.append(k)
                element = k
                local_rev_dict.pop(k)
                break
        if element == 0:
            raise KeyError("Haven't found empty set value")
        for (k, v) in local_rev_dict.items():
            v.discard(element)

    return result


test_rules = [[47, 53],
              [97, 13],
              [97, 61],
              [97, 47],
              [75, 29],
              [61, 13],
              [75, 53],
              [29, 13],
              [97, 29],
              [53, 29],
              [61, 53],
              [97, 53],
              [61, 29],
              [47, 13],
              [75, 47],
              [97, 75],
              [47, 61],
              [75, 61],
              [47, 29],
              [75, 13],
              [53, 13]]
test_updates = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47]]

assert sum_of_middle_page_numbers_from_correct_updates(test_rules, test_updates) == 143
assert sum_of_middle_page_numbers_for_corrected_updates(test_rules, test_updates) == 123

rules = []
scanningRules = True
updates = []
for line in sys.stdin:
    if scanningRules:
        if '|' in line:
            rules.append(list(map(int, line.split("|"))))
        else:
            scanningRules = False
    else:
        updates.append(list(map(int, line.split(','))))

print(sum_of_middle_page_numbers_from_correct_updates(rules, updates))
print(sum_of_middle_page_numbers_for_corrected_updates(rules, updates))
