def check_if_in_ranges(pattern_number, ranges):
    for range in ranges:
        if pattern_number >= range[0] and pattern_number <= range[1]:
            return True
    return False

def generate_num_patterns(max_value: int):
    pattern_number_array = []
    max_len = len(str(max_value))
    seen = set()

    for total_length in range(2, max_len + 1):
        for chunk_size in range(1, total_length // 2 + 1):
            if total_length % chunk_size != 0:
                continue

            repeats = total_length // chunk_size
            if repeats < 2:
                continue

            chunk_start = 10 ** (chunk_size - 1)
            chunk_end = 10 ** chunk_size

            for chunk in range(chunk_start, chunk_end):
                pattern_num_str = str(chunk) * repeats
                pattern_number = int(pattern_num_str)
                
                if pattern_number > max_value:
                    break

                if pattern_number in seen:
                    continue

                seen.add(pattern_number)
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

print(out)