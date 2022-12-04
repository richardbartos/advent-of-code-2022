import os.path

data_input = []


def find_complete_overlaps(data):
    """
    >>> find_complete_overlaps(["2-4,6-8",
    ... "2-3,4-5",
    ... "5-7,7-9",
    ... "2-8,3-7",
    ... "6-6,4-6",
    ... "2-6,4-8"])
    2
    """

    count = 0
    row_index = 0
    elf_matrix = []

    for item in data:
        whole_area = item.split(",")
        for half in whole_area:
            single_area = half.split("-")
            elf_matrix.append([int(x) for x in single_area])

    for i, item in enumerate(elf_matrix):
        row_index += 1

        if row_index % 2 == 0:
            if elf_matrix[i - 1][0] <= elf_matrix[i][0] and elf_matrix[i - 1][1] >= elf_matrix[i][1]:
                count += 1
            elif elf_matrix[i - 1][0] >= elf_matrix[i][0] and elf_matrix[i - 1][1] <= elf_matrix[i][1]:
                count += 1

    return count


def find_overlaps(data):
    """
    >>> find_overlaps(["2-4,6-8",
    ... "2-3,4-5",
    ... "5-7,7-9",
    ... "2-8,3-7",
    ... "6-6,4-6",
    ... "2-6,4-8"])
    4
    """

    count = 0
    row_index = 0
    elf_matrix = []

    for item in data:
        whole_area = item.split(",")
        for half in whole_area:
            single_area = half.split("-")
            elf_matrix.append([int(x) for x in single_area])

    for i, item in enumerate(elf_matrix):
        row_index += 1

        if row_index % 2 == 0:
            if elf_matrix[i - 1][1] >= elf_matrix[i][0] and elf_matrix[i - 1][0] <= elf_matrix[i][1]:
                count += 1
            elif elf_matrix[i - 1][0] <= elf_matrix[i][1] and elf_matrix[i - 1][1] >= elf_matrix[i][0]:
                count += 1

    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Total entirely overlapping assignments: " + str(find_complete_overlaps(data_input)))
    print("Total overlapping assignments: " + str(find_overlaps(data_input)))
