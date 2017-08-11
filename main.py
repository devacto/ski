#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: {} <map file>'.format(sys.argv[0]))

    print('Hello World!')

if __name__ == '__main__':
    main()