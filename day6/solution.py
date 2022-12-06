def check_if_all_unique(iter):
    results = []
    for x in iter:
        copy_list = list(iter).copy()
        copy_list.remove(x)
        results.append(x not in copy_list)
    return all(results)

def input_lookup_for_marker():
    input = open('input.txt').readline()
    for counter in range(len(input)):
        if check_if_all_unique(input[counter:counter+14]):
            return counter

if __name__ == '__main__':
    print(input_lookup_for_marker()+14)
