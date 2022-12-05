stacks = {
    1: 'stack_a',
    2: 'stack_b',
    3: 'stack_c',
    4: 'stack_d',
    5: 'stack_e',
    6: 'stack_f',
    7: 'stack_g',
    8: 'stack_h',
    9: 'stack_i'
}

stack_a = ['S', 'T', 'H', 'F', 'W', 'R']
stack_b = ['S', 'G', 'D', 'Q', 'W']
stack_c = ['B', 'T', 'W']
stack_d = ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J']
stack_e = ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z']
stack_f = ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G']
stack_g = ['Z', 'B', 'R', 'T', 'W', 'G', 'P']
stack_h = ['N', 'G', 'M', 'T', 'C', 'J', 'R']
stack_i = ['L', 'G', 'B', 'W']

def generate_instructions():
    """
    Generate instructions as three integers:
    - how many items to be moved
    - from which stack
    - to which stack
    """
    instructions = [line.strip() for line in open('input.txt').readlines()]
    for instruction in instructions:
        sub_instructions = instruction.split('move')[1].split('from')
        stack_pointers = sub_instructions[1].split('to')
        yield int(sub_instructions[0]), int(stack_pointers[0]), int(stack_pointers[1])

def execute_instruction(how_many, from_which, to_which):
    temp_stack = []
    for i in range(how_many):
        temp_stack.append(globals()[stacks[from_which]].pop())
    for i in range(len(temp_stack)):
        globals()[stacks[to_which]].append(temp_stack.pop())

def print_result():
    result = []
    for stack in stacks.values():
        result.append(globals()[stack][-1])

    print("".join(result))

if __name__ == '__main__':
    for how_many, from_which, to_which in generate_instructions():
        execute_instruction(how_many, from_which, to_which)

    print_result()
