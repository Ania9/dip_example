import fileinfo
f = fileinfo.FileInfo("d:/muzyka/Sabaton - Hearth of Iron.mp3")
print f

print f.__getitem__("name")

print f["name"]