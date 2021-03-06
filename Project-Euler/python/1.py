#!/usr/bin/env python


"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def run_calc():
    num = 1000
    results = []

    for x in range(1, num):
        if x % 3 == 0:
            results.append(x)
        elif x % 5 == 0:
            results.append(x)

    return sum(results)


def test_function():
    assert run_calc() == 233168


if __name__ == '__main__':
    test_function()
