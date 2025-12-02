out = 0
left_list = []
right_dict = {}
with open("input.txt", "r") as f:
    for line in f:
        elements = line.strip().split('   ')
        left_list.append(int(elements[0]))
        if elements[1] in right_dict:
            right_dict[int(elements[1])] += 1
        else:
            right_dict[int(elements[1])] = 1

for i in range(len(left_list)):
    out += left_list[i] * right_dict.get(left_list[i], 0)

print(out)