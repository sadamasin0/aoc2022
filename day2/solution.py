result_points = {
    'X': {
        'A': 3,
        'B': 1, 
        'C': 2
    },
    'Y': {
        'A': 4,
        'B': 5,
        'C': 6
    },
    'Z': {
        'A': 8,
        'B': 9,
        'C': 7
    }
}

total_points = 0

input = open('input.txt').readlines()

for round in input:
    choices = round.strip().split(' ')
    total_points += result_points[choices[1]][choices[0]]

print(total_points)