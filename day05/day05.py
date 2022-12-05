import os.path
import re

crate_dimension_x = 3
data_input = []

data_input_crane = []
data_input_length = []
data_input_operations = []


# def parse_data():


# if __name__ == "__main__":

with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as fh:
    for line in fh.readlines():
        data_input.append(line)

        if "[" in line:
            print(line[1])
            print(line[5])
            print(line[9])

        elif line.startswith(" 1"):
            print(re.sub(" +", " ", line)[1:])
        elif line.strip() != "":
            data_input_operations.append(line)

print(data_input_crane)
print(data_input_length)
print(data_input_operations)
