import os
print os.path.split("d:\\muzyka\\Sabaton - Hearts od Iron.mp3")
(filepath, filename) = os.path.split("d\\muzyka\\Sabaton - Hearts of Iron.mp3")
print filepath
print filename
(shortname, extension) = os.path.splitext(filename)
print shortname
print extension