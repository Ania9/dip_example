def foo(): print 4
foo()

foo.__doc__
print foo.__doc__ == None

print unicode(foo.__doc__)