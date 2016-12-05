# -*- coding: utf-8 -*-

'''
Day 1 of the Advent of Code challenge, parts A and B
'''

import sys


NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'

LEFT = 'L'
RIGHT = 'R'

MOVEMENTS = {
    (NORTH, LEFT): ((-1, 0), WEST),
    (NORTH, RIGHT): ((1, 0), EAST),

    (SOUTH, LEFT): ((1, 0), EAST),
    (SOUTH, RIGHT): ((-1, 0), WEST),

    (EAST, LEFT): ((0, 1), NORTH),
    (EAST, RIGHT): ((0, -1), SOUTH),

    (WEST, LEFT): ((0, -1), SOUTH),
    (WEST, RIGHT): ((0, 1), NORTH),
}


def calculate_distance(p1, p2):
    '''
    Calculate taxicab distance between two points on a city grid.
    '''
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def parse_path(text):
    '''
    Calculate distance between starting position and end of the path,
    specified by directions.
    '''
    parts = text.split(', ')
    heading = NORTH
    current_position = (0, 0)
    first_revisited = None
    visited = set()

    for part in parts:
        direction, steps = part[0], int(part[1:])
        delta, next_heading = MOVEMENTS[(heading, direction)]

        # We need
        for _ in xrange(steps):
            current_position = (
                current_position[0] + delta[0],
                current_position[1] + delta[1],
            )

            # We need to remember our first revisited point to complete Part B
            # (Easter Bunny waits for us at those coordinates)
            if current_position in visited and first_revisited is None:
                first_revisited = current_position
            visited.add(current_position)

        heading = next_heading

    return (
        calculate_distance((0, 0), current_position),
        calculate_distance((0, 0), first_revisited),
    )


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        directions = fp.read().strip()
        distance_to_end, distance_to_revisited = parse_path(directions)

        print 'Distances\n========='
        print 'First revisited point: {0}'.format(distance_to_revisited)
        print 'End of the path: {0}'.format(distance_to_end)