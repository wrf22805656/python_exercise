### exercise printing, printing

print ('\n exercise 8 \n')
formatter = "%r %r %r %r"
print (formatter % (1,2,3,4))
print (formatter % ('one', 'two', 'three', 'four'))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % ("I had this thing.", "That you could type up right.", "But it didn\'t sing", "So I said goodnight"))


### exercise 9
print ('\n exercise 9 \n')
# here are some new strange stuff, remember type it exactly
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("here are the days you need to work %r " %days)
print ("here are the days you need to work %s " %days)
print ("here are the days you need to work: ", days)

print ("here are the months:\n ",months)
print ("""There\'s something going on here.
with the three double-quotes.
we will be able to type as much as we like.
even 4 lines if we want,
or 5
or 6
""")



# exercise 10
print ("\n exercise10 \n")
print ("I am 6'2\" tall. ")
print ("I am 6'2\" tall")
print ('I am 6\'2" tall.')

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
print (tabby_cat)
print (persian_cat)
print (backslash_cat)


# here is a tiny piece of fun code to try out:
