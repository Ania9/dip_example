# -*- coding: utf-8 -*-
import odbchelper
object = odbchelper
method = 'buildConnectionString'
print getattr(object, method)
print getattr(object, method).__doc__