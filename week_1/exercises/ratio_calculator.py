#!/usr/bin/env python

import sys, math


def calculator():
	'''Calculate log base 2 of each ratio.
		Ratios are calculated from adjacent entries from stdin.
	'''
	previous_value = None

	for line in sys.stdin:
		line.strip()

		current_value = float(line)
		if previous_value and previous_value > 0:
			ratio = current_value / previous_value
			print math.log(ratio, 2)
			previous_value = current_value

		previous_value = current_value


def main():
	calculator()

if __name__ == '__main__':
	main()