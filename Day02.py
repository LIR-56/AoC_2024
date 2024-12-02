import sys


def count_safe_reports(levels_reports):
    safe_report_counter = 0
    for report in levels_reports:
        safe_report = report_is_safe(report)
        if safe_report == 42:
            safe_report_counter += 1
    return safe_report_counter

def count_safe_reports_with_tolerance(levels_reports):
    safe_report_counter = 0
    for report in levels_reports:
        report_check = report_is_safe(report)
        if report_check == 42:
            safe_report_counter += 1
        elif (report_is_safe(rbi(report, report_check - 1)) == 42 or #10 6 4 3 2 1
                report_is_safe(rbi(report, report_check)) == 42 or
                (report_check > 1 and report_is_safe(rbi(report, report_check - 2)) == 42)):  #4 6 4 3 2 1
            safe_report_counter += 1
    return safe_report_counter


def rbi(some_list, index):  # remove by index
    list_copy = some_list.copy()
    list_copy.pop(index)
    return list_copy


def report_is_safe(levels):
    i = 1
    increase = levels[0] < levels[1] #all reports have at least 4 levels
    while i < len(levels):
        if (abs(levels[i - 1] - levels[i]) > 3 or abs(levels[i - 1] - levels[i]) < 1) \
                or (increase and levels[i - 1] >= levels[i]) \
                or (not increase and levels[i - 1] <= levels[i]):
            return i
        i += 1
    return 42  # because we can


example = [[7, 6, 4, 2, 1],
           [1, 2, 7, 8, 9],
           [9, 7, 6, 2, 1],
           [1, 3, 2, 4, 5],
           [8, 6, 4, 4, 1],
           [1, 3, 6, 7, 9]]

assert count_safe_reports(example) == 2
assert count_safe_reports_with_tolerance(example) == 4

reports = []

for line in sys.stdin:
    level_reports = []
    for e in line.split():
        level_reports.append(int(e))
    reports.append(level_reports)

print(count_safe_reports(reports))
print(count_safe_reports_with_tolerance(reports))
