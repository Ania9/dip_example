f = open("d:/muzyka/Sabaton - Hearts of Iron.mp3", "rb")
print f
print f.tell()
f.seek(-128, 2)
print f.tell()
tagData = f.read(128)
print tagData
print f.tell()

print "-"*30

print f.closed
f.close()
print f
print f.closed
f.seek(0)
print f.tell()
print f.read()
print f.close()