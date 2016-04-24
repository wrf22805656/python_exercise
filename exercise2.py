# exercise 6
# A string is usually a bit of text you want to display to someone or "export" out of the
# the program you are writing.
# strings may contain the format characters you have discovered so far. you
# simply put the formatted variables in the string, and then a % (p[ercent )character, followed by the variable.

x = ('there are %d types of people.' % 10)
binary = 'binary'
do_not = 'don\'t'
y = "Those who know %s and those who %s." % (binary, do_not)
print ('\n exercise 6 \n')
print (x)
print (y)
print ("I said: %r." % x)
print ("I also said: \'%s\'. " %y)
print ("I also said: \'%r\'. " %y)

hilarious = False
joke_evaluation = 'Isn\'t that joke so funny?! %r'
print (joke_evaluation % hilarious)

w = "this is the left side of ..."
e = " a string with a right side."
print (w+e)

z = 1000
xx = ('there are %d types of people.' % z )
print (xx)
print ("I also said: %r" %xx )


# exercise 7

print ('\n exercise 7\n')
print ('Mary had a little lamb.')
print ('Its fleece was white as %s.' % 'snow')
print ('and everywhere that Mary went.')
print ('.' *10)
end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch that comma at the end. Try removng it to se what happens
print (end1 + end2 + end3 + end4 + end5 + end6,)
print (end7 + end8 + end9 + end10 +end11 +end12)
