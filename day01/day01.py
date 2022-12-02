import os.path

# setup list of sums for each elf
list_elf_calories = []

with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as fh:
    one_elf_calories = []

    for line in fh.readlines():
        line = line.strip()

        if line == "":
            list_elf_calories.append(sum(one_elf_calories))
            one_elf_calories = []
        else:
            one_elf_calories.append(int(line))

    # Add the last elf to the map as the "" is missing on the last line
    list_elf_calories.append(sum(one_elf_calories))

print("Number of calories carried by the most packed elf:")
print(max(list_elf_calories))

print("Number of calories of the three most packed elfs:")
if len(list_elf_calories) < 3:
    print("There are less than 3 elfs!")
else:
    list_elf_calories.sort(reverse=True)
    print(sum(list_elf_calories[0:2]))
