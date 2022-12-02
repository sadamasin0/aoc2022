shapes_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

result_points = {
    'X': {
        'A': 3,
        'B': 0, 
        'C': 6
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3
    }
}

total_points = 0

input = open('input.txt').readlines()

for round in input:
    choices = round.strip().split(' ')
    total_points += shapes_points[choices[1]] + result_points[choices[1]][choices[0]]

print(total_points)