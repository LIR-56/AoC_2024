def compact_and_get_resulting_checksum(short_disk_map):
    return get_checksum(compact(convert_to_full_map(short_disk_map)))


def convert_to_full_map(disk_map_short):
    disk_map_full = []
    i = 0
    while i < len(disk_map_short):
        if i % 2 == 0:
            j = int(disk_map_short[i])
            while j > 0:
                disk_map_full.append(int(int(i) / 2))
                j -= 1
        else:
            j = int(disk_map_short[i])
            while j > 0:
                disk_map_full.append(-1)
                j -= 1
        i += 1
    return disk_map_full


def compact(disk_map_full):
    i = 0
    j = len(disk_map_full) - 1
    while i < j:
        if disk_map_full[i] != -1:
            i += 1
        elif disk_map_full[j] == -1:
            j -= 1
        else:
            disk_map_full[i] = disk_map_full[j]
            disk_map_full[j] = -1
            i += 1
            j -= 1
    return disk_map_full


def get_checksum(full_compacted_disk_map):
    i = 0
    result = 0
    while i < len(full_compacted_disk_map):
        if full_compacted_disk_map[i] != -1:
            result += i * full_compacted_disk_map[i]
        i += 1
    return result


def compact_v2(disk_map_full):
    i = len(disk_map_full) - 1
    attempted_to_move = set()
    while i > 0:
        if disk_map_full[i] == -1 or disk_map_full[i] in attempted_to_move:
            i -= 1
        else:
            file_number = disk_map_full[i]
            attempted_to_move.add(file_number)
            j = i - 1
            while j >= 0 and disk_map_full[j] == disk_map_full[i]:
                j -= 1
            file_size = i - j
            k = 0
            found_free_space_for_file = False
            while k <= j:
                if disk_map_full[k] != -1:
                    k += 1
                else:
                    l = 0
                    while l < file_size:
                        if disk_map_full[k + l] != -1:
                            break
                        l += 1
                    if l == file_size:
                        found_free_space_for_file = True
                        break
                    else:
                        k += l
            if found_free_space_for_file:
                while file_size > 0:
                    disk_map_full[k] = file_number
                    disk_map_full[i] = -1
                    k += 1
                    i -= 1
                    file_size -= 1
            else:
                i -= file_size
    return disk_map_full


def compact_and_get_resulting_checksum_v2(short_disk_map):
    return get_checksum(compact_v2(convert_to_full_map(short_disk_map)))


assert compact_and_get_resulting_checksum("2333133121414131402") == 1928
assert compact_and_get_resulting_checksum_v2("2333133121414131402") == 2858

disk_map = input()
print(compact_and_get_resulting_checksum(disk_map))
print(compact_and_get_resulting_checksum_v2(disk_map))
