import os
print os.listdir("d:\\muzyka\\")
dirname = "c:\\"
print os.listdir(dirname)

print [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]
print [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]