#!/usr/bin/env python2
# encoding: utf-8

"""
Longest Lines.

Challenge Description:

Write a program to read a multiple line text file and write the 'N' longest
lines to stdout. Where the file to be read is specified on the command line.

Input sample:

Your program should read an input file (the first argument to your program will
be a path to a filename). The first line contains the value of the number 'N'
followed by multiple lines. You may assume that the input file is formatted
correctly and the number on the first line i.e. 'N' is a valid positive
integer. E.g.

2
Hello World
CodeEval
Quick Fox
A
San Francisco

Output sample:

The 'N' longest lines, newline delimited. Ignore all empty lines in the input.
Ensure that there are no trailing empty spaces on each line you print. Also
ensure that the lines are printed out in decreasing order of length i.e. the
output should be sorted based on their length. E.g.

San Francisco
Hello World

"""

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

num = int(test_cases[0])

lengths = {len(i): i for i in test_cases[1:] if i}
sorted_lengths = sorted(lengths.keys(), reverse=True)
for i in sorted_lengths[:num]:
    print(lengths[i])
