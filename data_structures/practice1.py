#!/usr/bin/env python3
def length_of_the_longest_string(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

