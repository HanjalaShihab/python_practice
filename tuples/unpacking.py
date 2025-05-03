thisTuple = ("amar", "nam", "hanjala")
(a, b, c) = thisTuple
print(a)
print(b)
print(c)



thisTuple = ("amar", "nam", "hanjala", "amar", "nam", "hanjala")
(a , b, *c) = thisTuple

print(a)
print(b)
print(c)


thisTuple = ("amar", "nam", "hanjala", "amar", "nam", "hanjala")
(a , *b, c) = thisTuple
print(a)
print(b)
print(c)