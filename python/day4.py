# -*- coding: utf-8 -*-

'''
Day 3 of the Advent of Code challenge, parts A and B
'''

from collections import Counter, namedtuple
import sys
import re


ROOM_ID_RE = re.compile(r'(?P<name>[a-z\-]+)(?P<id>\d+)\[(?P<checksum>[a-z]+)\]')
Room = namedtuple('Room', ('sector_id', 'checksum', 'name'))


def decrypt(string, key):
    result = []

    for c in string:
        if c == '-':
            decrypted = ' '
        else:
            decrypted = chr(ord('a') + ((ord(c) - ord('a')) + (key % 26)) % 26)
        result.append(decrypted)
    return ''.join(result)


def extract_room_info(room_descriptor):
    matches = ROOM_ID_RE.match(room_descriptor)

    name = matches.group('name')
    checksum = matches.group('checksum')
    sector_id = int(matches.group('id'))

    characters = Counter(name)
    characters.pop('-')

    frequencies = characters.items()

    # Here we sort by converting letter and its occurence into integer key,
    # weighted by letter frequency and penalized by its distance from
    # the start of the alphabet.
    sorted_letters = sorted(frequencies, key=lambda l: l[1] * 100 + 99 - ord(l[0]), reverse=True)
    calculated_hash = ''.join(map(lambda parts: parts[0], sorted_letters[:5]))

    if checksum == calculated_hash:
        return Room(sector_id, checksum, name)
    else:
        return None


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        rooms = fp.readlines()
        rooms = map(lambda l: l.strip(), rooms)

        real_rooms = filter(lambda l: l, map(extract_room_info, rooms))
        print 'Sum of valid sector IDs:', sum([room.sector_id for room in real_rooms])

        for room in real_rooms:
            decrypted_name = decrypt(room.name, room.sector_id).strip()
            if decrypted_name == 'northpole object storage':
                print 'North pole objects are stored in sector {0}'.format(room.sector_id)
                break
