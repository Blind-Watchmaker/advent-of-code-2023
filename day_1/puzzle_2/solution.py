import re

file_path = '../input.txt'

digit_str_to_numeric = {
    "zero": 0,
    "orez": 0,
    "one": 1,
    "eno": 1,
    "two": 2,
    "owt": 2,
    "three": 3,
    "eerht": 3,
    "four": 4,
    "ruof": 4,
    "five": 5,
    "evif": 5,
    "six": 6,
    "xis": 6,
    "seven": 7,
    "neves": 7,
    "eight": 8,
    "thgie": 8,
    "nine": 9,
    "enin": 9
}


def extract_digit(line, regex):
    pattern = re.compile(regex, re.IGNORECASE)
    matches = pattern.findall(line)
    if matches:
        digit = matches[0]
        # If digit is a string (e.g. "zero"), convert to string integer (e.g. '0').
        if digit in digit_str_to_numeric.keys():
            return str(digit_str_to_numeric[digit])
        # Otherwise, return the string integer (e.g. '1').
        return digit
    else:
        raise Exception("No digit found in the line!")
    
# Open the file and go through it line by line
forward_pattern = r'zero|one|two|three|four|five|six|seven|eight|nine|[0-9]'
backward_pattern = r'orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9]'
sum = 0
with open(file_path, 'r') as file:
    for line in file:
        # Strip leading and trailing whitespace
        line = line.strip()
        first_digit = extract_digit(line, forward_pattern)
        last_digit = extract_digit(line[::-1], backward_pattern)
        calibration_value = int(first_digit + last_digit)
        sum += calibration_value
        print(f"Input string: {line}")
        print(f"First digit: {first_digit}")
        print(f"Last digit: {last_digit}")
        print(f"Calibration value: {calibration_value}")
        print("")

print(f"Sum: {sum}")