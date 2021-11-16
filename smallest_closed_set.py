'''
This problem was asked by Google.
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them.
For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9],
one set of numbers that covers all these intervals is {3, 6}.
'''


def smallest_sets(*intervals):
    small_max = min([interval[1] for interval in intervals])
    large_min = max([interval[0] for interval in intervals])
    interval = sorted([small_max, large_min])
    print(interval)
    return interval


if __name__ == '__main__':
    smallest_sets([0, 3], [2, 6], [3, 4], [6, 9])
    smallest_sets([20, 20], [10, 15])
