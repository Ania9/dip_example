import sys
from fileinfo import MP3FileInfo
print MP3FileInfo.__module__

print sys.modules[MP3FileInfo.__module__]