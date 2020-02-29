#!/usr/bin/python3

class IntSeries:
	def is_part_of_series(self, lst):
		fsrs = dict()
		n = max(lst)
		if n < 1:
			print("n < 1\nTERMINATING...")
			exit()
		fsrs[0] = 0
		fsrs[1] = 1
		for x in range(2,n+1):
			fsrs[x] = 2*fsrs[x-1] - 2*fsrs[x-2]
		for k in lst:
			if k in fsrs.values():
				print("%s is part of the series."%k)
			else:
				print("%s is NOT part of the series."%k)

ints = IntSeries()
somelist = [1, 2, 5, 0, 3, 10, 13, -64, 32]
ints.is_part_of_series(somelist)
