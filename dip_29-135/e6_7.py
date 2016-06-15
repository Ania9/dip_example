logfile = open ('test.log', 'w')
logfile.write('udany test')
logfile.close()
print open('test.log').read()

logfile = open('test.log', 'a')
logfile.write(' linia 2')
logfile.close()
print open('test.log').read()