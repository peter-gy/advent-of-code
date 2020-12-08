def part_1(lines):
    pc = 0
    acc = 0
    executed = set()
    while True:
        if pc in executed:
            return acc
        else:
            executed.add(pc)
        line = lines[pc]
        instruction, argument = line.split()
        argument = int(argument)
        if instruction == 'jmp':
            pc += argument
            continue
        elif instruction == 'acc':
            acc += argument
        elif instruction == 'nop':
            pass

        pc += 1


def execute_program(lines):
    pc = 0
    acc = 0
    executed = set()
    while True:
        program_terminated = pc == len(lines)
        if program_terminated:
            return acc
        elif pc in executed:
            return None
        executed.add(pc)
        line = lines[pc]
        instruction, argument = line.split()
        argument = int(argument)
        if instruction == 'jmp':
            pc += argument
            continue
        elif instruction == 'acc':
            acc += argument
        elif instruction == 'nop':
            pass

        pc += 1


def part_2(lines):
    for i in range(len(lines)):
        lines_copy = lines[:]
        if 'jmp' in lines_copy[i]:
            lines_copy[i] = lines_copy[i].replace('jmp', 'nop')
        elif 'nop' in lines_copy[i]:
            lines_copy[i] = lines_copy[i].replace('nop', 'jmp')
        acc = execute_program(lines_copy)
        if acc is not None:
            return acc


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt', 'r')]
    print('Part 1:', part_1(lines))
    print('Part 2:', part_2(lines))

