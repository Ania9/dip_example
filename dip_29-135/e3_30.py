params = {"black":"cat", "pink":"elephant", "gray":"mouse"}
print ["%s=%s" % (k, v) for k, v in params.items()]
print ";".join(["%s=%s" % (k, v) for k, v in params.items()])