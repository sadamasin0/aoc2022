input = open('input.txt').readlines()

totals = []
this_sum = 0

for item in input:
    try:
        item_val = int(item)
        this_sum += item_val
    except ValueError:
        totals.append(this_sum)
        this_sum = 0

totals.sort(reverse=True)
print(sum(totals[:3]))

