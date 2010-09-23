
def first(a):
	return a[0]

def rest(a):
	return a[1:]

def last(a):
	return a[-1]

def null(a):
	return len(a) == 0

def cons(item, a):
	return [item] + a

def append(a, b):
	return a + b

def is_list(a):
	return type(a) == type([])
