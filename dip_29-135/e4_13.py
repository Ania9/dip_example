import odbchelper
print odbchelper.buildConnectionString
print "-"*50

print getattr(odbchelper, "buildConnectionString")
print "-"*50

object = odbchelper
method = "buildConnectionString"
print getattr(object, method)
print "-"*50

print type(getattr(object, method))
print "-"*50

import types
print type(getattr(object, method)) == types.FunctionType
print "-"*50

print callable(getattr(object, method))
print "-"*50