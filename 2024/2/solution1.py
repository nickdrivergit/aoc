out = 0
with open("input.txt", "r") as f:
    for line in f:
        is_safe = True
        elements = [int(item) for item in line.strip().split()]
        direction = 1 if elements[1] - elements[0] > 0 else -1
        for i in range(len(elements) - 1):
            diff = elements[i + 1] - elements[i]
            if diff == 0 or diff * direction <= 0 or abs(diff) > 3:
                is_safe = False
                break
        if is_safe == True:
            out += 1


print(out)