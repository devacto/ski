#!/usr/bin/env python

import sys, re

def parse_map(path):
    '''Creates a 2D array from the data, given the path.'''
    with open(path) as file:
        width, height = map(int, file.readline().split())
        grid = []
        for line in file:
            line = re.sub('[\n]', '', line)
            array = line.split(' ')
            grid.append(array)
    return width, height, grid

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: {} <map file>'.format(sys.argv[0]))

    # Parsing
    print('Parsing map data ...')
    w, h, g = parse_map(sys.argv[1])
    print('width = {}'.format(w))
    print('height = {}'.format(h))

    # Traversing
    for y in range(0, w):
        for x in range(0, h):
            list = []
            list.append(g[y][x])
            print('at x:{}, y:{} with value {}'.format(x, y, g[y][x]))
            print('up: {}; left: {}; right: {}, down: {}', )


if __name__ == '__main__':
    main()