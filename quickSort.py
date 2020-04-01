from typing import List
import random

def quickSort(ls : List[int]) -> List[int]:
	base = ls[len(ls) // 2]
	l = [x for x in ls if x < base]
	r = [x for x in ls if x > base]
	return l + [base] + r

if __name__ == '__main__':
	ls = []
	for i in range(1000):
		ls.append(random.randint(1,1000))
	print(quickSort(ls))