
import types
from listops import *
from operator import *
from readexp import *

dic ={}
def read():
    """ Calls the 'readexp' module and
       	retrive the input given by user in the list format
    """
    return getExp()

def definition(elements):
    """ If the first keyword is 'define',
       	this function adds the key to the environment
       	along with the value
    """
    dic[elements[1]] = elements[2]
    return 'added to env'

def function(elements):
    """ If the coming option is a method,
	either we will executen the lambda part simply 
	or will call the method again if it is recursive
    """
    a = dic[elements[0]]
    if type(a) == types.ListType:
        if a[0] == 'lambda':
	    i = 1
            for each in a[1]:
	        dic[each] = turningPoint(elements[i])
	        i += 1
	    return turningPoint(a[2])
	return a[0]
    return a

def condition(elements):
    """ The method returns either True or False
	or the corresponding value
	according to the request
    """
    if elements[1][0] == 'and':
	for each in elements[1][1:]:
	    if not calculate(each):
	        return calculate(elements[-1])
	return calculate(elements[-2])
    else:
	if calculate(elements[1]):
	    return turningPoint(elements[-2])
        return turningPoint(elements[-1])

def turningPoint(elements):
    """ The method checks for the if the
	first element retrieved from user is a 'define'
	or 'if' or already present in the environment or
	any other numeric value
    """
    if elements[0] == 'define':
	return definition(elements)
    elif elements[0] in dic:
        return function(elements)
    elif elements[0] == 'if':
        return condition(elements)
    else:
        ans = calculate(elements)
    return ans

def calculate(elements):
    """ Does all the calculations of the user input
    """
    global dic
    if type(elements) == types.ListType:
	op = first(elements)
	if op == '+':
	    f = add
	elif op == '-':
	    f = sub
	elif op == '*':
	    f = mul
	elif op == '/':
	    f = div
	elif op == '>':
	    f = gt	
	elif op == '<':
	    f = lt
	elif op == '=':
	    f = eq
	elif op == '>=':
	    f = ge
	elif op == '<=':
	    f = le
	f_op = calculate(elements[1])
	for each in elements[2:]:
	    f_op = f(f_op, calculate(each))
        return f_op
    elif elements.isalpha():
	return int(dic[elements])
    else:
    	return int(elements)

def main():
    try:
        while 1:
            elements = read()
            ans = turningPoint(elements)
            print ans
    except:
	print 'END OF SESSION!!!'

if __name__ == '__main__':
    main()

