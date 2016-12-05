# -*- coding: utf-8 -*-

'''
Day 1 of the Advent of Code challenge, parts A and B
'''

import sys

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


MOVEMENTS = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0),
}

EXAMPLE_KEYPAD = (
    '123',
    '456',
    '789',
)
REAL_KEYPAD = (
    '  1  ',
    ' 234 ',
    '56789',
    ' ABC ',
    '  D  ',
)


def determine_passcode(directions, keypad, start):
    # Usually we start at number '5' on a keypad
    position = start
    result = []
    width = len(keypad[0])
    height = len(keypad)

    for line in directions:
        for step in line:
            delta = MOVEMENTS[step]
            new_position = (position[0] + delta[0], position[1] + delta[1])

            if 0 <= new_position[0] < width and 0 <= new_position[1] < height:
                # Using whitespace as a marker allows us to support
                # both keypad shapes
                if keypad[new_position[1]][new_position[0]] != ' ':
                    position = new_position

        # We use inverse order of indexes because keypad symbols
        # are stored in rows
        result.append(keypad[position[1]][position[0]])

    return ''.join(result)


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        directions = fp.readlines()
        directions = map(lambda l: l.strip(), directions)

    example_passcode = determine_passcode(directions, EXAMPLE_KEYPAD, (1, 1))
    print 'Passcode for example keypad:', example_passcode

    real_passcode = determine_passcode(directions, REAL_KEYPAD, (0, 2))
    print 'Passcode for real keypad:', real_passcode
