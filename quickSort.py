from typing import List

def quickSort(ls : List[int]) -> List[int]:
	base = ls[len(ls) // 2]
	l = [x for x in ls if x < base]
	r = [x for x in ls if x > base]
	return l + [base] + r

if __name__ == '__main__':
	ls = [9, 5, 3, 8, 1, 10, 4, 11]
	print(quickSort(ls))