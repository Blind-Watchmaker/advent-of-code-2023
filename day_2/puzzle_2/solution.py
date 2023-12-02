import re
file_path = '../input.txt'

def extract_game_id(line):
    pattern = re.compile(r'Game (\d+):')
    matches = pattern.findall(line)
    return int(matches[0])

def remove_game_phrases(line):
    pattern = re.compile(r'Game (\d+):')
    return re.sub(pattern, '', line)

def capture_number_before_word(line, target_word):
    pattern = re.compile(r'(\d+)\s+' + re.escape(target_word))
    match = pattern.search(line)

    if match:
        return int(match.group(1))
    else:
        return 0

def extract_sets(line):
    # Split the line into entities based on semicolon
    sets = line.split(';')
    
    # Remove leading and trailing whitespaces from each entity
    sets = [set.strip() for set in sets]

    return sets

def extract_max_colour_counts(sets):
    colours = ["red", "green", "blue"]
    max_counts_per_colour = {}
    for colour in colours:
        colour_max_count = 0
        for set in sets:
            colour_count = capture_number_before_word(set, colour)
            if colour_count > colour_max_count:
                colour_max_count = colour_count
        max_counts_per_colour[colour] = colour_max_count
    return max_counts_per_colour

def determine_power(max_counts_per_colour):
    power = 1
    for key in max_counts_per_colour.keys():
        if max_counts_per_colour.get(key, 0) > 0:
            power *= max_counts_per_colour.get(key, 0)
    return power   
        
def analyze_game(line):
    # Strip leading and trailing whitespace.
    line = line.strip()

    # Extract the game_id.
    game_id = extract_game_id(line)

    # Lines begin with "Game {}:", so let's remove that.
    line = remove_game_phrases(line)

    # Sets are delimited by semicolons, so let's separate into sets.
    sets = extract_sets(line)

    # Let's use these sets to extract the maximum colour counts per colour.
    max_counts_per_colour = extract_max_colour_counts(sets)

    return determine_power(max_counts_per_colour)

with open(file_path, 'r') as file:
    powers = []
    for line in file:
        result = analyze_game(line)
        powers.append(result)
    print(sum(powers))