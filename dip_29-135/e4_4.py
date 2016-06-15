import odbchelper
from e4_1 import info
print info(odbchelper)
print "-"*50
print info(odbchelper, 12)
print "-"*50
print info(odbchelper, collapse=0)
print "-"*50
print info(spacing=15, object=odbchelper)