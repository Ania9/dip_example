from UserDict import UserDict

class FileInfo(UserDict):
    u"przechowuje metadane pliku"
    def __init__(selfself, filename=None):
        UserDict.__init__(self)
        self["name"] = filename
