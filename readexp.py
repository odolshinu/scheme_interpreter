
# Returns the user input as a list
char = ""

def getExp():
    """ Returns a list representation of given input
    """
    token = getToken()
    if not token == '(':return token
    a = []
    while 1:
        b = getExp()
	if b == ')': return a
	a.append(b)
        
def getToken():
    """ Returns a single character avoiding the leading spaces
    """
    while nextChar() <= ' ':getChar()
    a = getChar()
    if a in ['(',')']:return a
    while not nextChar() == ' ' and not nextChar() == ')' and not nextChar() == '\n':
        a = a + getChar()
    return a

def read():
    """ Returns the contents read from user
    """
    global char
    char =raw_input("$$$:") + '\n'
    return char
     
def nextChar():
    """ Returns the next character of user input
    """
    global char
    if char == "" :
	read()
    return char[0:1]

def getChar():
    """ Returns the first character of user input and deletes the character from the user input string forever
    """
    global char
    a = nextChar()
    char = char[1:]
    return a

