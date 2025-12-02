import time

start_time = time.perf_counter()

current_position = 50 #starting position
count = 0

with open("input.txt", "r") as f:
    for raw_line in f:
        line = raw_line.strip()
        dir = line[0]
        amt = int(line[1:])

        step = -1 if dir == 'L' else 1

        for i in range(amt):
            current_position = (current_position + step) % 100
            if current_position == 0:
                count += 1
    
print(f"Times at pos 0: {count} found in {time.perf_counter() - start_time} seconds")