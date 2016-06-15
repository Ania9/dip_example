try:
    fsock = open("d:/muzyka/Sabaton - Hearts of Iron.mp3", "rb", 0)
    try:
        fsock.seek(-128, 2)
        tagdata = fsock.read(128)
    finally:
        fsock.close()

except I0Error:
    pass