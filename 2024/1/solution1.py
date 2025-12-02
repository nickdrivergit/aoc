out = 0
left_list = []
right_list = []
with open("input.txt", "r") as f:
    for line in f:
        elements = line.strip().split('   ')
        left_list.append(elements[0])
        right_list.append(elements[1])
        # print(f"nums: {elements}")

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    out += abs(int(left_list[i]) - int(right_list[i]))

print(out)