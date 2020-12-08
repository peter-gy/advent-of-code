def execute_program(lines):
    pc = 0
    acc = 0
    executed = set()
    program_terminated = True
    while pc != len(lines):
        if pc in executed:
            program_terminated = False
            break
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
    return acc, program_terminated


def part_1(lines):
    return execute_program(lines)[0]


def part_2(lines):
    for i in range(len(lines)):
        lines_copy = lines[:]
        if 'jmp' in lines_copy[i]:
            lines_copy[i] = lines_copy[i].replace('jmp', 'nop')
        elif 'nop' in lines_copy[i]:
            lines_copy[i] = lines_copy[i].replace('nop', 'jmp')
        acc, program_terminated = execute_program(lines_copy)
        if program_terminated:
            return acc


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt', 'r')]
    print('Part 1:', part_1(lines))
    print('Part 2:', part_2(lines))
