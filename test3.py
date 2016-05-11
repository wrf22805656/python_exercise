#usr/bin/python

def diff21(n):
    if n > 21:
        return 2*abs(n-21)
    else:
	return abs(n-21)
print diff21(19) 


def parrot_trouble(time):
    if time < 7 or time >20:
	return True
    else:
	return False

print parrot_trouble(4)
