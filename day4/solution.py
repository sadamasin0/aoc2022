def generate_pairs():
    """
    Generate lines with no whitespaces
    """
    return [line.strip() for line in open('input.txt').readlines()]

def generate_list_from_range(str_range):
    """
    Generate list from given str range
    """
    range_edges = [int(x) for x in str_range.split('-')]
    return [x for x in range(range_edges[0], range_edges[1]+1)]

def check_if_any_range_contains_another(ranges):
    """
    Returns true if first range contains second or vice versa
    """
    range_first = generate_list_from_range(ranges[0])
    range_second = generate_list_from_range(ranges[1])
    return any([
        x in range_second for x in range_first
    ]) or any([
        x in range_first for x in range_second
    ])

if __name__ == '__main__':

    counter = 0

    for pair in generate_pairs():
        ranges = pair.split(',')
        if check_if_any_range_contains_another(ranges):
            counter += 1
    
    print(counter)
