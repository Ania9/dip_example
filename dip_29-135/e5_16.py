def __repr__(self): return repr(self.data)
def __cmp__(self, dict):
    if isinstance(dict, UserDict):
        return cmp(self.data, dict.data)
    else:
        return cmp(self.data, dict)
def __len__(self): return len(self.data)
def __delitem__(self, key): del self.data[key]

