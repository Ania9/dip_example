import fileinfo
f = fileinfo.FileInfo("d:/muzyka/Sabaton - Hearth of Iron.mp3")
print f
print "-"*30

f.__setitem__("gatunek", 31)
print f
print "-"*30

f["gatunek"]=32
print f
print "-"*30