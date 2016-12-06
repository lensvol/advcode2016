# -*- coding: utf-8 -*-

'''
Day 3 of the Advent of Code challenge, parts A and B
'''

import sys
import re


SIDES_RE = re.compile(r'[\s+]*(\d+)\s+(\d+)\s+(\d+)')


def parse_sides(text):
    matches = SIDES_RE.match(text)
    if matches is None:
        return -1, -1, -1

    return map(int, matches.groups())


def is_triangle_possible(given_sides):
    return all([
        given_sides[0] + given_sides[1] > given_sides[2],
        given_sides[0] + given_sides[2] > given_sides[1],
        given_sides[1] + given_sides[2] > given_sides[0],
    ])


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        triangles = fp.readlines()
        triangles = map(lambda l: l.strip(), triangles)

        regular_sides = map(parse_sides, triangles)
        possible_regular_triangles = filter(is_triangle_possible, regular_sides)
        print 'Possible conventional triangles:', len(possible_regular_triangles)