from string import ascii_letters

def generate_scoreboard():
    """
    Generate dict with score for each letter
    """
    scoreboard = {}
    i = 1
    for letter in ascii_letters:
        scoreboard[letter] = i
        i += 1
    return scoreboard

def generate_rucksacks():
    """
    Generate lines with no whitespaces
    """
    return [line.strip() for line in open('input.txt').readlines()]

def extract_shared_items(rucksack):
    """
    Returns set of unique shared items in rucksack compartments
    """
    middle = int(len(rucksack)/2)
    return {x for x in rucksack[:middle] if x in rucksack[middle:]}

def extract_shared_items_for_multiple_rucksacks(rucksacks):
    """
    Returns set of unique shared items in all given rucksacks
    """
    return {x for x in rucksacks[0] if all([x in y for y in rucksacks[1:]])}


if __name__ == '__main__':
    scoreboard = generate_scoreboard()
    rucksacks = generate_rucksacks()

    total_score = 0

    for i in range(0, len(rucksacks), 3):
        for shared_item in extract_shared_items_for_multiple_rucksacks(rucksacks[i:i+3]):
            total_score += scoreboard[shared_item]

    print(total_score)
