import os.path
import string

data_input = []


def count_rucksack_items(data):
    """
    >>> count_rucksack_items(["vJrwpWtwJgWrhcsFMMfFFhFp",
    ... "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    ... "PmmdzqPrVvPwwTWBwg",
    ... "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    ... "ttgJtRGJQctTZtZT",
    ... "CrZsJsPPZsGzwwsLwLmpwMDw"])
    157
    """

    count = 0
    for item in data:
        count += get_item_priorities(split_and_find_duplicates(item))

    return count


def split_and_find_duplicates(rucksack):
    """
    >>> split_and_find_duplicates("vJrwpWtwJgWrhcsFMMfFFhFp")
    'p'
    """

    first_compartment, second_compartment = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    for item in first_compartment:
        if item in second_compartment:
            return item
            # We're expecting there is always just one shared item and thus braking the loop early
            break


def find_duplicates_in_rucksacks(rucksacks):
    """
    >>> find_duplicates_in_rucksacks(["vJrwpWtwJgWrhcsFMMfFFhFp",
    ... "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    ... "PmmdzqPrVvPwwTWBwg"])
    'r'
    """

    for i, item in enumerate(rucksacks):
        rucksacks[i] = "".join(set(item))

    squashed_rucksacks = "".join(rucksacks)

    for character in squashed_rucksacks:
        if squashed_rucksacks.count(character) == 3:
            return character


def get_item_priorities(item):
    """
    >>> get_item_priorities("p")
    16
    """

    return string.ascii_letters.index(item) + 1


def count_elf_group_items(data):
    """
    >>> count_elf_group_items(["vJrwpWtwJgWrhcsFMMfFFhFp",
    ... "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    ... "PmmdzqPrVvPwwTWBwg",
    ... "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    ... "ttgJtRGJQctTZtZT",
    ... "CrZsJsPPZsGzwwsLwLmpwMDw"])
    70
    """

    count = 0
    bucket_three_elfs = []

    for item in data:
        if len(bucket_three_elfs) == 2:
            bucket_three_elfs.append(item)
            count += get_item_priorities(find_duplicates_in_rucksacks(bucket_three_elfs))
            bucket_three_elfs = []
        else:
            bucket_three_elfs.append(item)

    return count


with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as fh:
    for line in fh.readlines():
        line = line.strip()
        data_input.append(line)

print("Total sum of priorities of items in rucksack: " + str(count_rucksack_items(data_input)))

print("Total sum of priorities of items in elf group: " + str(count_elf_group_items(data_input)))
