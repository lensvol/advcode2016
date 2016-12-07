# -*- coding: utf-8 -*-

'''
Day 6 of the Advent of Code challenge, parts A and B
'''

import sys


def correct_errors(messages, modified=True):
    if not messages:
        return None

    letters = [dict() for _ in xrange(0, len(messages[0]))]

    for message in messages:
        for ind, character in enumerate(message):
            letters[ind][character] = letters[ind].get(character, 0) + 1

    result = [
        sorted(
            frequency.iteritems(),
            key=lambda it: it[1],
            reverse=modified,
        )[0][0]
        for frequency in letters
    ]

    return ''.join(result)


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        messages = fp.readlines()
        messages = map(str.strip, messages)

        print 'With repetition code:', correct_errors(messages)
        print 'With modified code:', correct_errors(messages, modified=False)
