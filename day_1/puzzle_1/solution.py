import re

file_path = '../input.txt'

def extract_digit(line):
    match = re.search(r'\d', line)
    if match:
        return match.group()
    else:
        raise Exception("No digit found in the line!")

# Open the file and go through it line by line
sum = 0
with open(file_path, 'r') as file:
    for line in file:
        # Strip leading and trailing whitespace
        line = line.strip()
        first_digit = extract_digit(line)
        last_digit = extract_digit(line[::-1])
        calibration_value = int(first_digit + last_digit)
        sum += calibration_value
        print(f"Input string: {line}")
        print(f"First digit: {first_digit}")
        print(f"Last digit: {last_digit}")
        print(f"Calibration value: {calibration_value}")
        print("")

print(f"Sum: {sum}")
