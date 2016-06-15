import os
print os.listdir("d:\\muzyka")

import glob
print glob.glob('d:\\muzyka\\*.mp3')
print glob.glob('d:\\muzyka\\a*.mp3')
print glob.glob('d:*\\*.mp3')