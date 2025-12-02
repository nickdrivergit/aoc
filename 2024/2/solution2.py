def is_safe(elements):
    diffs = [b - a for a, b in zip(elements, elements[1:])]
    if not diffs:
        return True

    if all(1 <= d <= 3 for d in diffs):
        return True
    if all(-3 <= d <= -1 for d in diffs):
        return True

    return False

out = 0
with open("input.txt", "r") as f:
    for line in f:      
        elements = [int(item) for item in line.strip().split()]
        if is_safe(elements):
            out += 1
            continue

        dampened_safe = False
        for i in range(len(elements)):
            shortened = elements[:i] + elements[i+1:]
            if is_safe(shortened):
                dampened_safe = True
                break

        if dampened_safe:
            out += 1


print(out)