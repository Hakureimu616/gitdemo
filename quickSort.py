def quickSort(ls):
	base = ls[len(ls) // 2]
	l = [x for x in ls if x < base]
	r = [x for x in ls if x > base]
	return l + [base] + r