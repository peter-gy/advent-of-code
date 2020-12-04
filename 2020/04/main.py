import re

regexes = {
    # at least 1920 and at most 2002
    'byr': r'^(?:19[2-9][0-9])|(?:200[0-2])$',
    # at least 2010 and at most 2020
    'iyr': r'^(?:201[0-9])|(?:2020)$',
    # at least 2020 and at most 2030
    'eyr': r'^(?:202[0-9])|(?:2030)$',
    # at least 150 and at most 193 cm OR at least 59 and at most 76 in
    'hgt': r'^(?:(?:1[5-8][0-9])|(?:19[0-3]))cm|(?:(?:59)|(?:6[0-9])|(?:7[0-6]))in$',
    # a # followed by exactly six characters 0-9 or a-f
    'hcl': r'^#[0-9a-f]{6}$',
    # exactly one of: amb blu brn gry grn hzl oth
    'ecl': r'^amb|blu|brn|gry|grn|hzl|oth$',
    # a nine-digit number, including leading zeroes
    'pid': r'^[0-9]{9}$'
}

ignored = ['cid']


def parse_passport_to_dict(passport):
    pairs = [tuple(pair.split(':')) for pair in re.split(r' |\n', passport)]
    return {key: value for (key, value) in pairs if key not in ignored}


def required_keys_are_present(passport):
    required_keys = regexes.keys()
    passport_dict_keys = parse_passport_to_dict(passport).keys()
    return len(required_keys) == len(passport_dict_keys)


def values_are_valid(passport):
    passport_dict = parse_passport_to_dict(passport)
    return all([re.match(regexes[key], value) for (key, value) in passport_dict.items()])


def part_1(passports):
    return sum([required_keys_are_present(passport) for passport in passports])


def part_2(passports):
    return sum([required_keys_are_present(passport) and values_are_valid(passport) for passport in passports])


if __name__ == '__main__':
    inp = open('input.txt', 'r').read()
    passports = inp.split('\n\n')
    print('part 1:', part_1(passports))
    print('part 2:', part_2(passports))
