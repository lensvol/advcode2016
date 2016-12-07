# -*- coding: utf-8 -*-

'''
Day 5 of the Advent of Code challenge, parts A and B
'''

from hashlib import md5
import sys


def calculate_first_password(door_id):
    index = 0
    characters_found = 0
    result = ['_'] * 8

    while characters_found < 8:
        hashed_value = md5(door_id + str(index)).hexdigest()
        if index % 1000 == 0:
            print '\r', ''.join(result), hashed_value,

        if hashed_value.startswith('00000'):
            result[characters_found] = hashed_value[5]
            characters_found += 1
        index += 1

    return ''.join(result)


def calculate_second_password(door_id):
    index = 0
    characters_found = 0
    result = ['_'] * 8

    while characters_found < 8:
        hashed_value = md5(door_id + str(index)).hexdigest()
        if index % 1000 == 0:
            print '\r', ''.join(result), hashed_value,

        if hashed_value.startswith('00000'):
            position, character = hashed_value[5], hashed_value[6]

            if position in '01234567' and result[int(position)] == '_':
                result[int(position)] = character
                print '\r', ''.join(result), hashed_value,
                characters_found += 1

        index += 1

    return ''.join(result)


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        door_id = fp.read().strip()

        password = calculate_first_password(door_id)
        print '\r---[ Password for the first door:', password, ']---'

        password = calculate_second_password(door_id)
        print '\r---[ Password for the second door:', password, ']---'
