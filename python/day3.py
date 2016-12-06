# -*- coding: utf-8 -*-

'''
Day 3 of the Advent of Code challenge, parts A and B
'''

from itertools import chain, islice, ifilter, tee
import sys
import re


SIDES_RE = re.compile(r'[\s+]*(\d+)\s+(\d+)\s+(\d+)')


def parse_sides(text):
    matches = SIDES_RE.match(text)
    if matches is None:
        return -1, -1, -1

    return map(int, matches.groups())


def is_triangle_possible(given_sides):
    '''
    Check to see if triangle is possible one
    (sum of any two sides should be greater than a remaining side)
    '''
    return all([
        given_sides[0] + given_sides[1] > given_sides[2],
        given_sides[0] + given_sides[2] > given_sides[1],
        given_sides[1] + given_sides[2] > given_sides[0],
    ])


def grouper(iterable, chunk_size):
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, chunk_size))
        if not chunk:
            return
        yield chunk


def extract_triangles_from_columns(sides):
    '''
    Transform incoming list of number tuples into
    list of numbers from columns.
    '''
    row_stream = chain(*sides)
    splits = tee(row_stream, 3)

    columns = chain(*[
        islice(split, start, None, 3)
        for start, split in enumerate(splits)
    ])

    return grouper(columns, 3)


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        triangles = fp.readlines()
        triangles = map(lambda l: l.strip(), triangles)

        sides = map(parse_sides, triangles)

        possible_regular_triangles = filter(is_triangle_possible, sides)
        possible_column_triangles = filter(is_triangle_possible, extract_triangles_from_columns(sides))

        print 'Possible conventional triangles:', len(possible_regular_triangles)
        print 'Possible triangles from columns:', len(possible_column_triangles)