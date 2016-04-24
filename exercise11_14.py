## exercise 11
# now it's time to pick up the pace, I have got you doing a lot of printing so you are used to typing simple things
# but those simple things are fairly boring.
# What we want to do now is get data into your programs.

print ('\t exercise11 \n')
print ("How old are you?")
age = input()
print ("How tall are you?")
height = input()
print ("How much do you weigh?")
weight = input()
print ("so, you're %r old, %r tall and %r heavy." % (age, height, weight))


## exercise 12
# when you typed raw_input(), you were typing the characters.
# which are parenthesis characters. This is similar to when you used them to do a format with extra
# variables as in "%s %s" % (x,y).

age = input("how old are you?")
height = input("How tall are you?")
weight = input ("How much do you weight?")

print ("so, you're %r old, %r tall and %r heavy." % (age, height, weight))