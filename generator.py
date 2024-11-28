import random


min_width = 1
max_width = 100
min_height = 1
max_height = 100
num_gates = 1000

#writing input file, the randomly generated values
with open("input.txt", "w") as f:
    for i in range(1, num_gates + 1):
        gate_name = "g"+str(i)
        width = random.randint(min_width, max_width)
        height = random.randint(min_height, max_height)
        f.write(f"{gate_name} {width} {height}\n")
