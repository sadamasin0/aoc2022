def generate_matrix_from_input():
    """ Returns matrix which can be accessed with result[row][col] """
    result = []
    for line in open('input.txt').readlines():
        result.append([
            int(x) for x in line.strip()
        ])
    return result

def check_if_tree_visible(tree_height, items_list):
    """ Check wheter given tree height is enough to be visible for given tree list """

    return tree_height > max(items_list)

if __name__ == '__main__':
    trees = generate_matrix_from_input()
    result = (len(trees) * 2 + len(trees[0]) * 2) - 4 # we can see all trees from the edges for sure

    for row_no, row in enumerate(trees):
        if row_no in [0, len(trees)-1]:
            continue
        for col_no, tree in enumerate(row):
            if col_no in [0, len(row)-1]:
                continue
            if any([
                # left
                check_if_tree_visible(tree, trees[row_no][:col_no]),
                # right
                check_if_tree_visible(tree, trees[row_no][col_no+1:]),
                # up
                check_if_tree_visible(tree, [trees[x][col_no] for x in range(row_no)]),
                # down
                check_if_tree_visible(tree, [trees[x][col_no] for x in range(row_no+1, len(trees))])
            ]):
                result += 1

    print(result)
