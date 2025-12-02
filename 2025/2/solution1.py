def check_if_in_ranges(pattern_number, ranges):
    for range in ranges:
        if pattern_number >= range[0] and pattern_number <= range[1]:
            return True
    return False

def generate_num_patterns(max_value: int):
    pattern_number_array = []
    max_len = len(str(max_value))

    for total_length in range (2, max_len + 1, 2):
        half_length = total_length // 2

        half_start = 10 ** (half_length - 1)
        half_end = 10 ** half_length
        
        factor = 10 ** half_length + 1

        for half in range(half_start, half_end):
            pattern_number = half * factor
            if pattern_number > max_value:
                break
            pattern_number_array.append(pattern_number)

    return pattern_number_array

def get_ranges():
    ranges = []
    with open("input.txt", "r") as f:
        for raw_line in f:
            ids = raw_line.strip().split(',')
            for id in ids:
                if not id:
                    continue
                range_start, range_end = id.split('-')
                ranges.append((int(range_start), int(range_end)))
    ranges.sort()
    return ranges

ranges = get_ranges()
max_number = ranges[-1][1]
pattern_numbers = generate_num_patterns(max_number)

out = 0
for num in pattern_numbers:
    if check_if_in_ranges(num, ranges):
        out += num

print(ranges)
print(max_number)
print(len(pattern_numbers))
print(out)